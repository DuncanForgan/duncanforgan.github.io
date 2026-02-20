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
  --theme-primary: #f97316;
  --theme-secondary: #fb923c;
  --theme-light: #ffedd5;
  --theme-border: #fdba74;
  
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  text-align: center;
  color: var(--theme-primary);
  margin-bottom: 2rem;
  border-bottom: 3px solid var(--theme-border);
  padding-bottom: 1rem;
}

.construction-notice {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  background-color: var(--theme-light);
  border: 2px solid var(--theme-border);
  border-radius: 8px;
  padding: 1rem 2rem;
  margin-bottom: 2rem;
}

.construction-notice p {
  margin: 0;
  color: var(--theme-primary);
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
