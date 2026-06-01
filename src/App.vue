<script setup>
</script>

<template>
  <div id="app">
    <nav class="main-nav">
      <router-link to="/" class="nav-link home">Home</router-link>
      <router-link to="/research" class="nav-link academic-research">I Was an Astrophysicist</router-link>
      <router-link to="/writing" class="nav-link writing">I Write Fiction</router-link>
      <router-link to="/software" class="nav-link software-engineering">I Write Code</router-link>
      <router-link to="/blog" class="nav-link blog">Blog</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  min-height: 100vh;
}

.main-nav {
  background-color: var(--nav-bar-color);
  padding: 1rem 2rem;
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: var(--nav-bar-text-color);
  text-decoration: none;
  font-weight: 600;
  padding: 0.5rem 1rem;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.nav-link:hover,
.nav-link.router-link-active {
  background-color: var(--theme-primary);
  color: var(--text-color);
}

</style>
