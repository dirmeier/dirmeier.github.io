<svelte:head>
  <title>Learning MLX with sabc · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">June 2026</p>
  <h1>Learning MLX</h1>
  <p class="lede">
    I've only recenly came across MLX, Apple's array framework.
    In comparison to JAX, my typical framework of choice, MLX features a proper C++ API making it particularly interesting. To explore the library a bit, I've implemented one of our recent publications,
    <a
      href="https://github.com/dirmeier/sabc"
      >SABC</a
    >, in MLX using its Python and C++ API.
  </p>

  <h2>Why MLX</h2>
  <p>
    MLX is a C++ library
    that you can link against directly, and which exposes Python bindings.     
    JAX is Python first, and anything C++ has to be done via
    Pallas or a custom XLA call. 
    That is, in MLX we can write
    compute-itensive code, like an MCMC sampler,
    in C++ and expose it to Python through <code>nanobind</code>.
    The Python bindings of MLX are held in the style of NumPy,
    and function transformations and a
    random number generator that requires explicitely setting keys.     
  </p>
  <p>
    Most of the Python API maps one to one onto JAX:
  </p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>purpose</th>
          <th>JAX</th>
          <th>MLX</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>array namespace</td>
          <td><code>jax.numpy</code> (<code>jnp</code>)</td>
          <td><code>mlx.core</code> (<code>mx</code>)</td>
        </tr>
        <tr>
          <td>vectorizing map</td>
          <td><code>jax.vmap</code></td>
          <td><code>mx.vmap</code></td>
        </tr>
        <tr>
          <td>autodiff</td>
          <td><code>jax.grad</code></td>
          <td><code>mx.grad</code></td>
        </tr>
        <tr>
          <td>PRNG key</td>
          <td><code>jax.random.key(seed)</code></td>
          <td><code>mx.random.key(seed)</code></td>
        </tr>
        <tr>
          <td>ahead-of-time compile</td>
          <td><code>jax.jit</code></td>
          <td><code>mx.compile</code></td>
        </tr>
        <tr>
          <td>structured control flow</td>
          <td><code>lax.scan</code>, <code>lax.cond</code>, <code>lax.fori_loop</code></td>
          <td>none — plain Python/C++ control flow</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
    JAX's control-flow primitives (<code>lax.fori_loop</code>,
    <code>lax.scan</code>, ...) are necessary because a 
    <code>jit</code>ted function compiles to one static graph. A Python <code>for</code>
    or <code>if</code> on a traced value cannot go inside that graph, so the
    loop or the branch has to be written as a primitive the tracer can
    capture. 
  </p>  
  <p>
    For instance, let's look at Newton's method in JAX:
  </p>
  <pre><code class="language-python">from jax import lax
import jax.numpy as jnp

def newton(f, df, x, n_iter=20):
  def body(_, x):
    step = jnp.where(jnp.abs(df(x)) &gt; 1e-12, f(x) / df(x), 0.0)
    return x - step
  return lax.fori_loop(0, n_iter, body, x)</code></pre>
  <p>
    MLX has no trace, so the same function is an ordinary Python
    loop:
  </p>
  <pre><code class="language-python">import mlx.core as mx

def newton(f, df, x, n_iter=20):
  for _ in range(n_iter):
    step = mx.where(mx.abs(df(x)) &gt; 1e-12, f(x) / df(x), 0.0)
    x = x - step
  return x</code></pre>
  <p>
    And because <code>MLX</code> is a C++ library, the same loop compiles
    straight into C++:
  </p>
  <pre><code class="language-cpp">mx::array newton(const std::function&lt;mx::array(mx::array)&gt;&amp; f,
                 const std::function&lt;mx::array(mx::array)&gt;&amp; df,
                 mx::array x, int n_iter = 20) &lbrace;
  for (int i = 0; i &lt; n_iter; ++i) &lbrace;
    mx::array step = mx::where(
        mx::greater(mx::abs(df(x)), mx::array(1e-12f)),
        mx::divide(f(x), df(x)), mx::array(0.0f));
    x = mx::subtract(x, step);
  &rbrace;
  return x;
&rbrace;</code></pre>
  <p>
    The other primitives translate the same way. A <code>lax.scan</code>
    is a loop that accumulates.
    For instance, let's consider exponential moving average in JAX:
  </p>
  <pre><code class="language-python">def ema(xs, alpha):
  def step(carry, x):
    y = alpha * x + (1 - alpha) * carry
    return y, y
  _, ys = lax.scan(step, xs[0], xs)
  return ys</code></pre>
  <p>
    In MLX the carry is a plain variable and the scan is a plain loop:
  </p>
  <pre><code class="language-python">def ema(xs, alpha):
  carry = xs[0]
  ys = []
  for x in xs:
    carry = alpha * x + (1 - alpha) * carry
    ys.append(carry)
  return mx.stack(ys)</code></pre>
  <p>
    Each MLX op is lazy, so a plain loop builds a
    graph that keeps growing until <code>mx.eval</code> evaluates it (i.e., actually computes a value).
    However, similarly to JAX,
    <code>mx.compile</code> can still compile a function into a single graph when
    throughput is needed.
  </p>

  <h2>The benchmark</h2>
  <p>
    I've compared SABC in MLX against a JAX version, and a NumPy version and a
    Numba version from a collaborator: <code>sbijax</code>,
    <code>sabc-mlx</code>, <code>sabc-numpy</code>, <code>sabc-numba</code>.
    The table below shows wall time, compile time, peak RSS, and W₁ distance
    to an MCMC reference posterior on the <code>two_moons</code> task (the best
    value in each column is in bold).
  </p>
  <div class="table-wrap">
    <table>
      <thead>
        <tr>
          <th>algorithm</th>
          <th>wall s</th>
          <th>compile s</th>
          <th>peak RSS MB</th>
          <th>W₁ to ref</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>sbijax (JAX)</td>
          <td><strong>0.32</strong></td>
          <td>1.54</td>
          <td>546</td>
          <td><strong>0.019</strong></td>
        </tr>
        <tr>
          <td>sabc-mlx</td>
          <td>1.40</td>
          <td><strong>0.00</strong></td>
          <td><strong>52</strong></td>
          <td>0.021</td>
        </tr>
        <tr>
          <td>sabc-numpy</td>
          <td>0.50</td>
          <td><strong>0.00</strong></td>
          <td>137</td>
          <td>0.024</td>
        </tr>
        <tr>
          <td>sabc-numba</td>
          <td>0.39</td>
          <td>0.45</td>
          <td>186</td>
          <td>0.021</td>
        </tr>
      </tbody>
    </table>
  </div>
  <p>
    All four implementations recover the reference posterior faithuflly.  
    Post-compile, JAX runs about 4x faster than MLX. MLX wins on memory:
    10x less, because there is no XLA buffer pool and no JIT cache. 
  </p>
  <h2>Conclusion</h2>
  <p>
    In summary, even when factoring in the compile time I think I am still sticking to JAX.
    But I will definitely use MLX more often in the future 👾🍏.
  </p>
</article>

