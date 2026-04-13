<template>
  <div class="home">    
    <h1>Dr Duncan Forgan PhD</h1>
    <p>🚧 This is my new website which is currently under construction</p>    
    <div class="nav-links">
      <router-link to="/blog" class="btn">Read My Blog Posts</router-link>
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

.construction-notice {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  background-color: #fff3cd;
  border: 2px solid #ffc107;
  border-radius: 8px;
  padding: 1rem 2rem;
  margin-bottom: 2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.construction-notice h2 {
  margin: 0;
  color: #856404;
  font-size: 1.5rem;
}

.construction-icon {
  font-size: 2rem;
}

h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: #42b883;
}

p {
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 1rem;
}

.subtitle {
  font-size: 1rem;
  color: #999;
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
