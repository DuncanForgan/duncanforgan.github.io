<template>
  <div class="home">
    <h1>Welcome to My Blog</h1>
    <p>This is a Vue 3 static website with dynamic routing for blog posts.</p>
    <div class="nav-links">
      <router-link to="/blog" class="btn">View Blog Posts</router-link>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.home {
  text-align: center;
  padding: 2rem;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #42b883;
}

p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
}

.nav-links {
  margin-top: 2rem;
}

.btn {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #42b883;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn:hover {
  background-color: #35a372;
}
</style>
