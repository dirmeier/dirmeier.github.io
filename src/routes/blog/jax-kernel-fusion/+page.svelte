<script>
  import katex from 'katex';
  import 'katex/dist/katex.min.css';

  const tex = (s, display = false) =>
    katex.renderToString(s, { displayMode: display, throwOnError: false });
</script>

<svelte:head>
  <title>JAX kernel fusion · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">August 2026</p>
  <h1>JAX kernel fusion</h1>
  <p class="lede">Evaluating JAX kernel fusion using XLA, Pallas and CUDA FFI.</p>
  <p>
      When writing a JAX function and running it on a GPU, the XLA compiler usually
      tries to fuse operations into a single kernel launch. This sometimes works well, 
      but often we need to write custom Pallas or low-level CUDA kernels to do in manually. Here, we evaluate using Pallas
      and JAX' foreign function interface to bridge to a custom CUDA kernel. We'll test all this
      using a simple QK-Norm+ROPE operation which one typically finds in the attention mechanisms
      of modern LLMs.
  </p>
  <h2>QK-Norm+ROPE</h2>
  <p>
    Let
    {@html tex('q \\in \\mathbb{R}^{B \\times S \\times H \\times D}')} be the query
    vector of a self-attention mechanism. If {@html tex('x = q[b, s, h, :]')} is a
    single attention head vector, QK-Norm+ROPE first normalises over the head dimension
  </p>
  {@html tex(
    '\\mu = \\frac{1}{D}\\sum_d x_d^2, \\qquad \\hat{x}_d = \\frac{x_d}{\\sqrt{\\mu+\\varepsilon}}\\,g_d,',
    true
  )}
  <p>
    and then rotates each channel {@html tex('i')} against its partner
    {@html tex('i+m')}, where {@html tex('m = D / 2')}, by an angle that depends
    on the sequence position {@html tex('s')},
  </p>
  {@html tex(
    '\\begin{pmatrix} y_i \\\\ y_{i+m}\\end{pmatrix} = \\begin{pmatrix} \\cos s\\theta_i & -\\sin s\\theta_i \\\\ \\sin s\\theta_i & \\cos s\\theta_i\\end{pmatrix}\\begin{pmatrix} \\hat{x}_i \\\\ \\hat{x}_{i+m}\\end{pmatrix},',
    true
  )}
  <p>
    where {@html tex('\\theta_i = \\Theta^{-2i/D}')} and {@html tex('\\Theta')} is
    some constant.
  </p>


  <h2>From <code>jaxpr</code> to HLO to PTX/SASS</h2>
  <p>
  To understand what XLA is doing, let's examine the entire path from Python to machine code, i.e.:
  </p>
<pre><code>Python -> jaxpr -> StableHLO -> HLO -> PTX/SASS</code></pre>
  <p>In plain JAX, the QK-Norm+ROPE operation looks like this:</p>
  <pre
    ><code class="language-python"
      >def qk_norm_rope(query, gamma, cos, sin, EPS=1e-6):
  mean_square = jnp.mean(jnp.square(query), axis=-1, keepdims=True)
  qn = query * jax.lax.rsqrt(mean_square + EPS) * gamma

  half = query.shape[-1] // 2
  lo, hi = qn[..., :half], qn[..., half:]
  c = cos[None, :, None, :]
  s = sin[None, :, None, :]
  return jnp.concatenate([lo * c - hi * s, hi * c + lo * s], axis=-1)</code
    ></pre
  >
  <p
    >Tracing this (<code>jaxpr</code>) give us this:</p
  >
  <pre
    ><code
      >&lbrace; lambda ; a:f32[2,32,4,128] b:f32[128] c:f32[32,64] d:f32[32,64]. let
    e:f32[2,32,4,128] = square a
    f:f32[2,32,4] = reduce_sum[axes=(3,) out_sharding=None] e
    g:f32[2,32,4,1] = broadcast_in_dim[broadcast_dimensions=(0, 1, 2)] f
    h:f32[2,32,4,1] = div g 128.0:f32[]
    i:f32[2,32,4,1] = add h 9.999999974752427e-07:f32[]
    j:f32[2,32,4,1] = rsqrt i
    k:f32[2,32,4,128] = mul a j
    l:f32[1,1,1,128] = broadcast_in_dim[broadcast_dimensions=(3,)] b
    m:f32[2,32,4,128] = mul k l
    n:f32[2,32,4,64] = slice[
      limit_indices=(2, 32, 4, 64)
      start_indices=(0, 0, 0, 0)
      strides=None
    ] m
    o:f32[2,32,4,64] = slice[
      limit_indices=(2, 32, 4, 128)
      start_indices=(0, 0, 0, 64)
      strides=None
    ] m
    p:f32[1,32,1,64] = broadcast_in_dim[broadcast_dimensions=(1, 3)] c
    q:f32[1,32,1,64] = broadcast_in_dim[broadcast_dimensions=(1, 3)] d
    r:f32[2,32,4,64] = mul n p
    s:f32[2,32,4,64] = mul o q
    t:f32[2,32,4,64] = sub r s
    u:f32[2,32,4,64] = mul o p
    v:f32[2,32,4,64] = mul n q
    w:f32[2,32,4,64] = add u v
    x:f32[2,32,4,128] = concatenate[dimension=3] t w
  in (x,) &rbrace;</code
    ></pre
  >

  <p>
    The <code>jaxpr</code> shows that JAX records 20 primitive operations.
    It doesn't matter if we use vanilla JAX, Pallas calls or FFI calls: all are JAX
    primitives that are being traced yielding a <code>jaxpr</code> as a first step. 
    However, the 3 implementations take 3 different "routes" in order to
    produce machine code (shown below with the help of Gemini):
  </p>
  <pre
    ><code>  route 1                route 2                  route 3
  XLA, compiler-fused               Pallas                CUDA via FFI

  jnp ops in Python      kernel fn in Python      qk_norm_rope.cu in C/CUDA
        |                        |                       |
      jaxpr                pallas_call             nvcc, at BUILD time
        |                        |                       |
    StableHLO           StableHLO custom_call   StableHLO custom_call
        |                 @mosaic_gpu_v2         @qk_norm_rope_cuda
        |                        :                       :
        |                        :                       :
        |                        :                       :
        |                        :                       :
    HLO passes                  HLO                     HLO
    (fusion decided)      custom-call, target=   custom-call, target=
        |                 mosaic_gpu_v2          qk_norm_rope_cuda
        |                        |                       |
        |                        |                       |
        |                        |                       |
    Triton IR              Mosaic GPU                    |
    (on GH200)             MLIR -> NVVM                  |
        |                        |                       |
        |                        |                       |
     LLVM IR                     |                       |
        +----------------------- + ----------------------+
                                 |
                                PTX          virtual ISA
                                 |
                               ptxas         compiles/optimizes PTX for a specific architecture
                                 |
                                SASS         real machine code for sm_90</code
    ></pre
  >

  <p>
    For vanilla JAX Python code, after tracing, the <code>jaxpr</code> is lowered to StableHLO, JAX' HLO dialect,
    from where it is to lowered HLO, the specific intermediate representations (IRs) of the XLA compiler.
    The HLO (at least with some caveats) shows how many kernels each
    implementation launches per call which can be used as a diagnostic tool. Importantly,
    a <code>fusion</code> represents exactly one kernel launch, while a
    <code>custom-call</code> represents an unknown number of them. 
    </p><p>
    When we <code>jit</code> the <code>qk_norm_rope</code> function on an GH200,
    XLA produces the following HLO fusing everything into a <b>single</b> kernel operation:
  </p>
  <pre
    ><code
      class="language-diff">  ENTRY %main.2 (q, g, cos, sin) -> f32[4,1024,16,128] &lbrace;
+   ROOT %fusion.9 = f32[4,1024,16,128] fusion(%sin.1, %cos.1, %g.1, %q.1),
+       kind=kCustom, calls=%fused_computation.7,
        backend_config=&lbrace;"fusion_backend_config":&lbrace;
          "kind":"__triton",
          "block_level_fusion_config":&lbrace;
            "num_warps":"8","output_tiles":[&lbrace;"sizes":["4","2","16","64"]&rbrace;]&rbrace;&rbrace;&rbrace;
  &rbrace;</code
    ></pre
  >
  <p>
  The HLO shows that XLA uses OpenAI's Triton utilizing 8
    warps (8 x 32 threads) and an output tile shape of
    <code>[4, 2, 16, 64]</code>. 
</p>
  <p>
    Let's also a look at the CUDA HLO:
  </p>
  <pre
    ><code
      class="language-diff">  ENTRY %main.1 (q.1: f32[4,1024,16,128], g.1: f32[128], cos.1: f32[1024,64], sin.1: f32[1024,64]) -> f32[4,1024,16,128] &lbrace;
    %sin.1 = f32[1024,64]&lbrace;1,0&rbrace; parameter(3)
    %cos.1 = f32[1024,64]&lbrace;1,0&rbrace; parameter(2)
    %g.1 = f32[128]&lbrace;0&rbrace; parameter(1)
    %q.1 = f32[4,1024,16,128]&lbrace;3,2,1,0&rbrace; parameter(0)
+   ROOT %ffi_call.1 = f32[4,1024,16,128]&lbrace;3,2,1,0&rbrace; custom-call(%q.1, %g.1, %cos.1, %sin.1), custom_call_target="qk_norm_rope_cuda", operand_layout_constraints=&lbrace;f32[4,1024,16,128]&lbrace;3,2,1,0&rbrace;, f32[128]&lbrace;0&rbrace;, f32[1024,64]&lbrace;1,0&rbrace;, f32[1024,64]&lbrace;1,0&rbrace;&rbrace;, api_version=API_VERSION_TYPED_FFI, metadata=&lbrace;op_name="jit(cuda_qk_norm_rope)/ffi_call" scheduling_name="ffi_call.1" stack_frame_id=4&rbrace;, backend_config=&lbrace;&rbrace;
&rbrace;</code
    ></pre
  >
  <p>
    As expected (since it was defined this way <a
      href="https://github.com/dirmeier/jax-kernel-fusion/blob/main/cuda/qk_norm_rope.cu"
      >here</a
    >), there is only a single primitive.
  </p>


  <p>Now, more interestingly, the HLO of the tiled Pallas kernel:</p>
  <pre
    ><code
      class="language-diff">  ENTRY %main.1 (q.1: f32[4,1024,16,128], g.1: f32[128], cos.1: f32[1024,64], sin.1: f32[1024,64]) -> f32[4,1024,16,128] &lbrace;
    %sin.1 = f32[1024,64]&lbrace;1,0&rbrace; parameter(3)
    %cos.1 = f32[1024,64]&lbrace;1,0&rbrace; parameter(2)
    %g.1 = f32[128]&lbrace;0&rbrace; parameter(1)
    %q.1 = f32[4,1024,16,128]&lbrace;3,2,1,0&rbrace; parameter(0)
    %bitcast.2 = f32[4096,2048]&lbrace;1,0&rbrace; bitcast(%q.1), metadata=&lbrace;op_name="q" scheduling_name="bitcast.2"&rbrace;
+ %wrapped_broadcast = f32[64,128]&lbrace;1,0&rbrace; fusion(%g.1), kind=kLoop, calls=%wrapped_broadcast_computation, metadata=&lbrace;op_name="jit(tiled_qk_norm_rope)/broadcast_in_dim" scheduling_name="wrapped_broadcast" stack_frame_id=4&rbrace;, backend_config=&lbrace;"device_type":"DEVICE_TYPE_INVALID","force_earliest_schedule":false,"native_emitter_backend_config":&lbrace;"type":"NATIVE_EMITTER_TYPE_INVALID","unroll_factor":0&rbrace;,"operation_queue_id":"0","reification_cost":[]&rbrace;
+ %pallas_call.1 = f32[4096,2048]&lbrace;1,0&rbrace; custom-call(%bitcast.2, %wrapped_broadcast, %cos.1, %sin.1), custom_call_target="mosaic_gpu_v2", operand_layout_constraints=&lbrace;f32[4096,2048]&lbrace;1,0&rbrace;, f32[64,128]&lbrace;1,0&rbrace;, f32[1024,64]&lbrace;1,0&rbrace;, f32[1024,64]&lbrace;1,0&rbrace;&rbrace;, api_version=API_VERSION_TYPED_FFI, metadata=&lbrace;op_name="jit(tiled_qk_norm_rope)/pallas_call" scheduling_name="pallas_call.1" stack_frame_id=5&rbrace;, backend_config=&lbrace;kernel_hash = "...", module = "&lt;truncated 149369 bytes&gt;", use_custom_barrier = false, uses_xla_collective_metadata = false&rbrace;
  ROOT %bitcast.1.0 = f32[4,1024,16,128]&lbrace;3,2,1,0&rbrace; bitcast(%pallas_call.1), metadata=&lbrace;op_name="jit(tiled_qk_norm_rope)/pallas_call" scheduling_name="bitcast.1.0" stack_frame_id=5&rbrace;
&rbrace;</code
    ></pre
  >
  <p>
  Even though there is a <code>custom-call</code> within the <code>pallas_call</code> primitive, we are 
  only looking at a single kernel launch, since Pallas compiles every kernel through
  Mosaic's <code>_lower_as_gpu_kernel</code> which corresponds to exactly one CUDA kernel.
</p>

<h2>Runtimes</h2>  
  <p>  
    I ran the three implementations on a GH200 (which uses a
    H100 Hopper GPU) using the query dimensionality <code
      >(128, 1024, 16, 128)</code
    >. Results are shown below:
  </p>
  <table>
    <thead>
      <tr><th>Mode</th><th>ms</th><th>GB/s</th><th>vs XLA</th></tr>
    </thead>
    <tbody>
      <tr
        ><td>XLA</td><td>0.840</td><td>2555.2</td><td>1.00x</td
        ></tr
      >      
      <tr><td>Pallas</td><td>0.833</td><td>2577.3</td><td>1.01x</td></tr>
      <tr
        ><td>CUDA</td><td>0.600</td><td>3576.6</td><td>1.40x</td
        ></tr>      
    </tbody>
  </table>
<p>
  The example operations (QK-Norm+ROPE) is fairly trivial and the cache hierarchy of the 
  H100 already solves many problems we would typically see, so the numbers are a bit
  misleading. Interestingly though, our Pallas implementation runs as fast as the XLA compiled one.
  Our custom CUDA kernel which we access via <code>jax.ffi</code> almost runs 1.4 times as 
  fast as the XLA baseline. 
  CUDA wins by assigning one warp (32 threads) to each head vector, rather than forcing it across 128 lanes. This ensures all 128
  channels live safely in the registers of a single warp, requiring no workarounds.
</p>
  <h2>Conclusion</h2>
  <p>
    Here, we developed QK-Norm+ROPE implementations using vanilla JAX, Pallas and CUDA FFI, and evaluated how XLA lowers them to HLO.
    Surprisingly (and counter-intuitively), I found the FFI path significantly easier thatn the Pallas approach. 
    The results of the runtime measurements were expectedly unconclusive, given
    the simplicity of the operation and the consequential kernel fusion that was achieved by XLA.
    In addition to gaining a better understanding of HLO and Pallas, there's also some insights I've gained:
  </p>  
  <ul>
    <li>
      A <code>fusion</code> is exactly one kernel launch while a <code>custom-call</code> launches an unknown number.
    </li>
    <li>
      <code>copy</code>, <code>transpose</code> or <code>concatenate</code>
      outside a fusion are real kernels, and usually mark where fusion was blocked.
      </li>
    <li>
      Compare pre- and post-optimisation HLO with <code>--xla_dump_to</code>. If they look similar, 
      XLA fused little or nothing, which is worth investigating.             
    </li>
    <li>
      HLO for the same code differs per architecture: on my M1 it yielded three fusions while it was a single fusion on a GH200.
    </li>    
    <li>
    Consider the actual hardware architecture that you work with. If the data fits into the cache, using SMEM does not increase throughput.      
    </li>    
  </ul>
  <p>
    The code is on <a href="https://github.com/dirmeier/jax-kernel-fusion">GitHub</a>.
    Hope reading this was informative to some 🙂🦉.
  </p>
</article>
