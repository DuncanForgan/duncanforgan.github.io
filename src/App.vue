<script setup>
</script>

<template>
  <div id="app">
    <nav class="main-nav">
      <router-link to="/" class="nav-link home">Home</router-link>
      <router-link to="/research" class="nav-link academic-research">I Was an Astrophysicist</router-link>
      <router-link to="/writing" class="nav-link writing">I Write Fiction</router-link>
      <router-link to="/software" class="nav-link software-engineering">I Write Code</router-link>
      <router-link to="/blog" class="nav-link blog">I Blog</router-link>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  min-height: 100vh;
}



</style>
