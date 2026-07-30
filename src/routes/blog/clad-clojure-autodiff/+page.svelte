<svelte:head>
  <title>Reverse-mode autodiff in Clojure · Simon Dirmeier</title>
</svelte:head>

<article class="post">
  <p class="post-date">May 2022</p>
  <h1>Reverse-mode autodiff in Clojure</h1>
  <p class="lede">
  <i>A proper computer scientist needs to know a Lisp</i> - some opinionated computer scientist.    
  </p>

  <h2>Learning Clojure the ML way</h2>
  <p>
  In order to learn Clojure, or at least get a feel for it, I recently implemented a proof-of-concept reverse-mode AD framework in it:
  <a href="https://github.com/dirmeier/clad">clad</a>.
    </p>
    <p>
    <code>clad</code> represents the computation graph
    as an adjacency matrix (via <code>core.matrix</code>) and a
    map of nodes. The forward/backward passes of a function are two topological
    traversals over it: we compute <code>-bottom-up</code> to compute values and
    <code>-top-down</code> to accumulate adjoints:
  </p>
  <pre><code class="language-clojure">(defn grad [f idx]
  (let [graph (expr/expression-graph f)]
    (fn [&amp; y]
      (let [graph (-top-down (-bottom-up (-set-values graph y)))]
        (:adjoint
         (nth
          (filter
           (fn [node] (:is-variable node))
           (vals (into (sorted-map) (:nodes graph))))
          idx))))))</code></pre>
  <p>
    Each call to the returned function rebuilds the graph's value/adjoint
    state from scratch rather
    than mutating a shared structure in place. This is not really efficient, but good enough for 
    the sake of learning functional programming.
  </p>

  <p>The published API is a single <code>grad</code> function:</p>
  <pre><code class="language-clojure">(require '[clad.core :refer [grad]])

(defn f [x y]
  (/ (- 1.0 (Math/exp (- x)))
     (+ 1.0 (Math/exp (- y)))))

(def g ((grad f 0) 2.0 1.0))
;; => 0.0989</code></pre>
  <p>
    <code>(grad f 0)</code> returns the derivative of <code>f</code> with
    respect to its argument at index <code>0</code> (here, <code>x</code>),
    evaluated at the point <code>(2.0 1.0)</code>.
  </p>
  
  <h2>Conclusion</h2>
  <p>
  I learned a functional language when I studied CS (<a href="https://en.wikipedia.org/wiki/Standard_MLl">Standard ML</a>), 
  but always found them a bit "academic" and didn't give much thought to them. When learning Clojure, my
  opinionated view changed a bit.
  Quoting from Peter Norvig's <a href="https://www.norvig.com/21-days.html">blog</a>: <i>A language that doesn't affect the way you think about programming, is not worth knowing</i>.
  In that sense, while I will never use Clojure professionally, 
  learning it definitely gave me a new view on functional programming. 
  
  </p>
</article>

