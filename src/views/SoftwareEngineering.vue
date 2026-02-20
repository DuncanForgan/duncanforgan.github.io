<template>
  <div class="software-engineering">
    <h1>Software Engineering</h1>
    <div class="construction-notice">
      <span class="construction-icon">🚧</span>
      <p>This section is under construction</p>
      <span class="construction-icon">🚧</span>
    </div>
    <p class="intro">Software projects and engineering work will be showcased here.</p>
  </div>
</template>

<script setup>
</script>

<style scoped>
.software-engineering {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  text-align: center;
  color: #42b883;
  margin-bottom: 2rem;
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
}

.construction-notice p {
  margin: 0;
  color: #856404;
  font-weight: 600;
}

.construction-icon {
  font-size: 1.5rem;
}

.intro {
  text-align: center;
  font-size: 1.1rem;
  color: #666;
}
</style>
