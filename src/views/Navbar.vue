<template>
  <nav
    class="navbar has-shadow is-fixed-top"
    role="navigation"
    aria-label="main navigation"
  >
    <div class="container">
      <div class="navbar-brand">
        <a
          role="button"
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navlist"
          onclick="document.querySelector('#navlist').classList.toggle('is-active');"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navlist" class="navbar-menu" style="margin-right: 50px">
        <div class="navbar-end">
          <a class="navbar-item is-tab" href="/#home">Home</a>
          <a class="navbar-item is-tab" href="/#contact">Contact</a>
        </div>
      </div>
    </div>
  </nav>
</template>
