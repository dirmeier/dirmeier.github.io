<svelte:head>
  <title>What is DiffusionGemma? · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">August 2026</p>
  <h1>What is DiffusionGemma?</h1>
  <p class="lede">
    To continue my journey learning MLX and stay up to date with discrete diffusion language models,
    I started reimplementing
    <a href="https://deepmind.google/models/gemma/diffusiongemma/">DiffusionGemma</a>.
    Initially I was assuming it was a large-scale <a href="https://arxiv.org/abs/2503.09573">BD3LM</a>.
    However, when going deeper into some references and the original code, it looks like a combination
    of multiple recent models. In this blog post, what reveal how DiffusionGemma actually is :).
  </p>
  <h2>There is no paper</h2>
  <p>
    DiffusionGemma is a 26B-A4B mixture-of-experts model that generates text
    by denoising a block of tokens in parallel instead of decoding left to
    right. It shipped without a research paper. I read the
    <a href="https://ai.google.dev/gemma/docs/diffusiongemma/model_card">model card</a>,
    the vLLM write-up, the
    <a href="https://github.com/NVIDIA-NeMo/Automodel/blob/main/docs/guides/dllm/diffusiongemma.md">NeMo guide</a>,
    and the
    <a href="https://github.com/google-deepmind/gemma/tree/main/gemma/diffusion">reference implementation</a>.
    None of them cite an arXiv ID. They agree on four points:
  </p>
  <ul style="list-style-type: circle;">
    <li>
      Corruption replaces tokens with <i>uniform-random vocabulary tokens</i>.
      There is no <code>[MASK]</code> token.
    </li>
    <li>
      The denoiser can condition on its own previous prediction
      (self-conditioning), mixed in per example during training.
    </li>
    <li>
      Generation is block-autoregressive: a 256-token block is denoised
      bidirectionally, committed to the KV cache, and the next block is
      conditioned on it.
    </li>
    <li>
      Denoising is entropy-bounded: confident positions are kept, the rest are
      renoised with random tokens.
    </li>
  </ul>
  <p>
    DiffusionGemma corrupts tokens by uniform-random replacement. BD3LM, like
    the <a href="https://arxiv.org/abs/2406.07524">MDLM</a> line it builds on,
    uses masked (absorbing) noise instead.
  </p>

  <h2>UDLM and BD3LM combined</h2>
  <p>
    The
    <a href="https://kuleshov-group.github.io/blog/blog/2026/how-to-build-a-diffusion-language-model/">Kuleshov group</a>,
    who authored BD3LM, describe DiffusionGemma as a uniform-state diffusion
    model (<a href="https://arxiv.org/abs/2412.10193">UDLM</a>) that uses
    block diffusion for generation. The recipe combines two of their papers:
  </p>
  <ul style="list-style-type: circle;">
    <li>
      The block-autoregressive structure (denoise a block, commit it, start the
      next) comes from BD3LM.
    </li>
    <li>
      The uniform-state noise and the D-CFG guidance come from UDLM.
    </li>
    <li>
      <a href="https://arxiv.org/abs/2506.10892">Duo</a> develops the same
      uniform-state process further, deriving it from an underlying Gaussian
      diffusion and adding fast self-conditioned sampling.
    </li>
  </ul>

  <h2>Block diffusion is a framework</h2>
  <p>
    Block diffusion is a framework with a block-size dial: block size 1 is
    autoregression, block size equal to sequence length is full diffusion,
    and everything between is a mix. The dial is independent of the noise
    process. BD3LM uses the masked process, DiffusionGemma the uniform one.
  </p>
  <p>
    DiffusionGemma is therefore a special case of block diffusion but not of
    BD3LM: citing BD3LM alone describes the generation loop correctly but not
    the noise process.
  </p>

  <h2>Design axes</h2>
  <p>
    The table lists models as columns and the choices that define a
    discrete-diffusion LM as rows.
  </p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>axis</th>
          <th>MDLM</th>
          <th>BD3LM</th>
          <th>UDLM</th>
          <th>Duo</th>
          <th>DiffusionGemma</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>noise state</td>
          <td>masked</td>
          <td>masked</td>
          <td>uniform</td>
          <td>uniform</td>
          <td>uniform</td>
        </tr>
        <tr>
          <td>generation</td>
          <td>single block</td>
          <td>block-AR</td>
          <td>single block</td>
          <td>single block</td>
          <td>block-AR</td>
        </tr>
        <tr>
          <td>attention</td>
          <td>bidirectional</td>
          <td>block-causal</td>
          <td>bidirectional</td>
          <td>bidirectional</td>
          <td>causal prefill, bidir. denoise</td>
        </tr>
        <tr>
          <td>self-conditioning</td>
          <td>no</td>
          <td>no</td>
          <td>no</td>
          <td>yes</td>
          <td>yes</td>
        </tr>
        <tr>
          <td>guidance</td>
          <td>—</td>
          <td>—</td>
          <td>D-CFG</td>
          <td>—</td>
          <td>D-CFG</td>
        </tr>
        <tr>
          <td>variable length</td>
          <td>no</td>
          <td>yes</td>
          <td>no</td>
          <td>no</td>
          <td>yes</td>
        </tr>
        <tr>
          <td>backbone</td>
          <td>encoder</td>
          <td>encoder</td>
          <td>encoder</td>
          <td>encoder</td>
          <td>Gemma-4 MoE</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
    DiffusionGemma combines UDLM's noise row with BD3LM's generation row,
    adding self-conditioning and an MoE backbone.
  </p>

  <h2>Attention and variable length</h2>
  <p>
    The reference code establishes two properties, neither of which is a
    block-causal attention mask.
  </p>
  <p>
    First, attention inside a block is bidirectional. In
    <code>create_decoder_attention_mask</code> the condition for a key position
    is <code>kv_canvas_id &lt;= selected_canvas_idx</code>, independent of the
    query position, so every query sees the whole current block. The
    streaming sampler in <code>_sampler.py</code> uses a plain
    <code>jnp.ones((B, L, L))</code> block mask for the same reason.
  </p>
  <p>
    Second, across blocks it is block-causal: block <code>i</code> sees the
    prompt and blocks <code>j &lt;= i</code>, never a future block. The
    variable length comes from growing the K and V matrices, not from this
    mask. A finished block is written to the cache with
    <code>append_tokens_to_cache</code>, and the next block attends to the
    committed history through a validity mask
    (<code>arange(cache_length) &lt; total_valid</code>) that tracks how many
    cache slots are filled.
  </p>
  <p>
    The block-causal mask applies to both training and sampling, per its
    docstring. The only difference is the number of query positions: training
    scores all blocks in one pass, sampling processes one block at a time.
    Sampling one block at a time means future blocks are simply absent from
    the cache, so the streaming sampler reproduces the same causal structure
    without an explicit future mask. Neither path applies a causal mask inside
    a block.
  </p>

  <h2>What my code has, and what it needs</h2>
  <p>
    <a href="https://github.com/dirmeier/block-diffusion-mlx">block-diffusion-mlx</a>
    already has the uniform-state denoiser: uniform corruption with no mask
    token, an <code>x0</code>-prediction cross-entropy loss, self-conditioning,
    an entropy-based sampler, and a Gemma-4 MoE backbone. That is the
    within-block model of DiffusionGemma, and it is UDLM, not BD3LM.
  </p>
  <p>
    What it does not have yet is the block-autoregressive loop. Attention is
    bidirectional over a single 256-token block and there is no KV cache to
    carry history between blocks. Generating longer than one block requires a
    growing KV cache and a commit-and-continue loop.
  </p>

  <h2>Building the block-autoregressive loop</h2>
  <p>
    The block-autoregressive loop requires a <code>block_size</code>
    parameter, a KV cache that grows one block at a time, and a training mask
    scoring all blocks in a single forward pass; the mask follows directly
    from <code>create_decoder_attention_mask</code>. I verified the cache with
    a direct equivalence test:
  </p>
  <pre><code class="language-python">def test_cache_matches_dense_forward():
  tokens = random_tokens(block_size * 2)
  dense_out, _ = model(tokens, mask=block_causal_mask(len(tokens), block_size))

  block0, block1 = tokens[:block_size], tokens[block_size:]
  _, cache = model(block0, mask=None)
  cached_out, _ = model(block1, cache=cache, offset=block_size)

  assert allclose(dense_out[block_size:], cached_out)</code></pre>
  <p>
    A dense forward over both blocks must equal a cached forward over the
    second block with the first committed. The
    <code>block_size == seq_len</code> case is kept as a regression test and
    reproduces v1's output exactly.
  </p>

  <h2>Diagnosing slow convergence</h2>
  <p>
    DiffusionGemma's release is inference-only, so the training objective —
    mean cross-entropy of <code>model(x_t)</code> against <code>x0</code> —
    is not specified by DeepMind. This loss matches what
    <a href="https://arxiv.org/abs/2412.10193">UDLM</a> calls
    <code>use_simple_ce_loss</code> and was not the cause of the convergence
    problem.
  </p>
  <p>
    The causes were a constant learning rate with no warmup (the v2 design
    specified cosine decay, which the training script did not implement) and
    independent per-example sampling of <code>t ~ U(0, 1)</code>, which
    produces batches near <code>t ≈ 0</code> or <code>t ≈ 1</code> with little
    training signal. Neither is visible in the per-step training loss, which
    is noisy by construction. The fixes: a fixed held-out batch and PRNG key
    evaluated every 100 steps as a convergence metric, antithetic stratified
    sampling of <code>t</code> following UDLM, and a warmup-then-cosine-decay
    learning-rate schedule.
  </p>

  <h2>Reading the reference more closely</h2>
  <p>
    v2 implemented the items listed as open knobs in the v1 design: QK-norm,
    alternating sliding/global attention, dual RoPE bases, and the MoE
    shared-dense branch. v3 followed from a line-by-line re-read of the
    Gemma4 source and identified three further discrepancies:
  </p>
  <ul style="list-style-type: circle;">
    <li>
      <code>skip_scale</code>: every reference block ends with
      <code>outputs * self.skip_scale</code>, a learnable scalar initialised
      to one.
    </li>
    <li>
      a third RMSNorm: the reference also normalises <code>value</code>
      (<code>with_scale=False</code>), in addition to query and key.
    </li>
    <li>
      per-layer embeddings (PLE): the general Gemma4 layer averages a learned
      <code>(token, layer)</code> table with a projection of the token
      embedding, but the diffusion forward pass sets
      <code>ignore_ple_tokens=True</code>, which uses only the projection. A
      direct port of the general layer would allocate a table that is never
      read.
    </li>
  </ul>
  <p>
    The self-conditioning module had the same kind of discrepancy: it was
    implemented as a single linear layer, against the reference's
    <code>pre_norm → GeGLU FFN → add → post_norm (no scale)</code>. The
    reference also passes an explicit zero tensor on the first denoising step
    rather than omitting the module; the two are numerically equivalent but
    produce different computational graphs.
  </p>

  <h2>Generalizing the package: bd to d3pm</h2>
  <p>
    By v3, <code>src/bd/</code> implemented a single denoiser under a general
    package name. Uniform-state diffusion is one instance of a broader family
    that includes MDLM's and BD3LM's masked-state processes. The package was
    renamed <code>bd</code> to <code>d3pm</code>, after
    <a href="https://arxiv.org/abs/2107.03006">Austin et al.</a>, in
    anticipation of adding further models such as MDLM or Duo.
  </p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>surface</th>
          <th>visibility</th>
          <th>why</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>d3pm</code> core + models</td>
          <td>public, flat</td>
          <td>the whole point of the library</td>
        </tr>
        <tr>
          <td><code>d3pm.nn</code></td>
          <td>public, sub-package</td>
          <td>a toolkit users compose from</td>
        </tr>
        <tr>
          <td><code>d3pm._src.models</code></td>
          <td>private</td>
          <td>complete models are terminal artifacts, not building blocks</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
    Models are imported by name (<code>from d3pm import DiffusionGemma</code>);
    internal file layout is not part of the public interface. The restructure
    also removed a dependency from the core loss:
    <code>block_diffusion_loss</code> previously computed a toy
    uppercase-label for classifier-free guidance internally, coupling it to
    the Shakespeare example. That computation moved to the example code;
    <code>block_diffusion_loss</code> now accepts an externally supplied
    conditioning label, or none.
  </p>
</article>
