<svelte:head>
  <title>Sharding blaxbird models over a mesh · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">July 2026</p>
  <h1>Sharding blaxbird models over a mesh</h1>
  <p class="lede">
    <a href="https://github.com/dirmeier/blaxbird">blaxbird</a> is a
    high-level API for building and training Flax NNX models without the usual
    JAX/Flax verbosity. Version 0.2.0 adds mesh-based sharding: FSDP, tensor
    parallelism, expert parallelism, or any combination thereof.
  </p>

  <h2><code>jax.sharding.Mesh</code> + <code>jax.sharding.PartitionSpec</code></h2>
  <p>
    To train a model in parallel in NNX, we need to define three things: sharding annotation, 
    a mesh, and a data partitionspec.
    Parameter-sharding is read directly from its
    <code>nnx.with_partitioning</code> annotation. The parallelism strategy
    therefore lives with in model definition, and <code>train_fn</code> needs
    only a <code>jax.sharding.Mesh</code> and a <code>PartitionSpec</code> for
    the data axis:
  </p>
  <pre><code class="language-python">from jax.sharding import Mesh, PartitionSpec as P
from jax.experimental import mesh_utils
from blaxbird import train_fn

mesh = Mesh(mesh_utils.create_device_mesh((4, 2)), ("fsdp", "tp"))
with mesh:
  train = train_fn(
    fns=(train_step, val_step), mesh=mesh,
    data_partition_spec=P("fsdp"), ...
  )
  train(rng_key, optimizer, train_itr, val_itr)</code></pre>
  <p>
    Moving from a single device to a 2D FSDP+TP mesh is a one-line change.
    Neither <code>train_step</code>/<code>val_step</code> nor
    the model definition change: the sharding strategy is a property of the
    mesh shape and the model's <code>nnx.with_partitioning</code> annotations.
  </p>

  <h2>Two reference models</h2>
  <p>
    The repo features to distributed training examples in <a
      href="https://github.com/dirmeier/blaxbird/tree/main/examples/llm"
      ><code>examples/llm</code></a
    > using two LMs with different parallelism definitions:
  </p>
  <ul style="list-style-type: circle;">
    <li>
      <strong>Gemma4</strong>: sharded
      over a 2D mesh (FSDP + TP).
    </li>
    <li>
      <strong>Qwen3Next</strong>: top-2-of-8 sparse
      MoE over a 3D mesh (FSDP + TP + expert).
    </li>
  </ul>
</article>

