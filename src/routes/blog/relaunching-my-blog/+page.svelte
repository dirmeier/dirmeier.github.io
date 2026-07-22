<svelte:head>
  <title>🌈👾🦉Relaunching my blog🦉👾🌈 · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">July 2026</p>
  <h1>🌈👾🦉Relaunching my blog🦉👾🌈</h1>  
  <p>
    After having been approached by several people (well, three, actually) in the last couple of months for 
    old blog posts of mine,
    I've decided to both make the blog public again and to relaunch it altogether.
  </p>
  <p>
    My older blog posts were mainly concerned with probabilistic and causal models
    (like tensor smoothers or copula processes). The new series will be mainly about 
    deep learning (particularly generative models), reinforcement learning and HCP, such as:
  </p>
  <ul style="list-style-type: circle;">
    <li><b>Large-scale DL with JAX and Flax</b>: 
    Some blog posts will feature how to use JAX/Flax to do large-scale GPU training of deep learning models, including
    FSDP, TP, and PP strategies, how to analyse and optimize training using tools such as Xprof and Nvidia Nsight,
    and what the terms XLA, HLO, LLVM IR, etc. mean.
    </li>
    <li><b>Recent RL algorithms like SPO and GSPO</b>: Gonna look into how recent algorithms like Simple Policy 
    Optimization (SPO) and Group Sequence Policy Optimization (GSPO) changed the landscape of reinforcement learning.
    </li>
    <li><b>Generative models</b>: 
    Some blog posts will OF COURSE be on LLMs and various architectures, diffusion models, diffusion LMs, and multi-modality.
    </li>
      <li><b>Refreshing vector and matrix intrinsics skills</b>: 
    Since recently I was mainly (but very rarely) doing GPGPU programming (e.g., CUDA), some blog posts will aim
    at refreshing some SIMD intrinsics skills using SME2 (as supported by Mac M4/M5 and newer Armv9.x-A (like Arm Neoverse) chips). 
    I've done vectors intrinsics programming using AVX on x64 processors in the past but haven't had an Intel CPU
    in years, and modern data centers and clouds (I think) are often built on Arm Neoverse.
    </li>  
    <li><b>Apple's MLX</b>:
    Array frameworks like JAX, and how they implement reverse-mode and 
    forward-mode autodiff efficiently, have been one of my favourite things
    for a while, so some of the posts will feature Apple's new framework MLX to elucidate
    how useful it can be for small-scale DL like typically found in, e.g., inverse problems
    or probabilistic programming. The fact that it has a proper C++ API (unlike JAX) makes it even more interesting.    
    </li>
  </ul>
</article>

