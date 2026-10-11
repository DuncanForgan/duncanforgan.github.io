<template>
  <div class="blog">
    <h1>Blog Posts</h1>
    <div class="year-controls">
      <button type="button" class="year-toggle-all" @click="toggleAll">
        {{ allOpen ? 'Collapse all' : 'Expand all' }}
      </button>
    </div>
    <section v-for="group in groups" :key="group.year" :id="group.year" class="year-section">
      <button
        type="button"
        class="year-header"
        :aria-expanded="isOpen(group.year)"
        @click="toggle(group.year)"
      >
        <span class="chevron" :class="{ open: isOpen(group.year) }">▸</span>
        <span class="year">{{ group.year }}</span>
        <span class="count">{{ group.posts.length }} {{ group.posts.length === 1 ? 'post' : 'posts' }}</span>
      </button>
      <div v-show="isOpen(group.year)" class="posts">
        <div v-for="post in group.posts" :key="post.slug" class="post-card">
          <h2>{{ post.title }}</h2>
          <p class="date">{{ post.date }}</p>
          <p class="excerpt">{{ post.excerpt }}</p>
          <router-link :to="`/blog/${post.slug}`" class="read-more">Read More →</router-link>
        </div>
      </div>
    </section>
    <div class="nav-links">
      <router-link to="/" class="btn-back">← Back to Home</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { blogPosts } from '../config/blogPosts'

const groups = computed(() => {
  const byYear = new Map()
  for (const post of blogPosts) {
    const year = post.date.slice(0, 4)
    if (!byYear.has(year)) byYear.set(year, [])
    byYear.get(year).push(post)
  }
  return [...byYear.entries()]
    .sort((a, b) => b[0].localeCompare(a[0]))
    .map(([year, posts]) => ({ year, posts }))
})

// Latest year open by default, or the year in the URL hash (e.g. /blog#2011)
const hashYear = window.location.hash.slice(1)
const initial = groups.value.some((g) => g.year === hashYear)
  ? hashYear
  : groups.value[0]?.year
const open = ref(new Set(initial ? [initial] : []))

const isOpen = (year) => open.value.has(year)
const toggle = (year) => {
  const next = new Set(open.value)
  next.has(year) ? next.delete(year) : next.add(year)
  open.value = next
}
const allOpen = computed(() => open.value.size === groups.value.length)
const toggleAll = () => {
  open.value = allOpen.value ? new Set() : new Set(groups.value.map((g) => g.year))
}
</script>

<style scoped>
.year-controls {
  text-align: right;
  margin-bottom: 1rem;
}

.year-toggle-all {
  background: none;
  border: none;
  cursor: pointer;
  text-decoration: underline;
  font: inherit;
}

.year-section {
  margin-bottom: 1rem;
}

.year-header {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.75rem 1rem;
  background-color: #f0f0f0;
  color: #333;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  cursor: pointer;
  font: inherit;
  text-align: left;
  margin-bottom: 1rem;
}

.year-header:hover {
  background-color: #e0e0e0;
}

.year {
  font-size: 1.25rem;
  font-weight: 700;
}

.count {
  margin-left: auto;
  font-size: 0.9rem;
}

.chevron {
  display: inline-block;
  transition: transform 0.2s;
}

.chevron.open {
  transform: rotate(90deg);
}

.posts {
  display: flex;
  flex-direction: column;
  gap: 2rem;
}

.post-card {
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  padding: 1.5rem;
  transition: box-shadow 0.3s;
}

.post-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.post-card h2 {
  margin-top: 0;  
}

.date {
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.excerpt {  
  line-height: 1.6;
}

.read-more {
  display: inline-block;
  margin-top: 1rem;
  text-decoration: none;
  font-weight: 600;
}

.nav-links {
  margin-top: 2rem;
  text-align: center;
}

.btn-back {
  display: inline-block;
  padding: 0.75rem 1.5rem;
  background-color: #f0f0f0;
  color: #333;
  text-decoration: none;
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn-back:hover {
  background-color: #e0e0e0;
}
</style>
