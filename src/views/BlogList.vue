<template>
  <div class="blog-list">
    <h1>Blog Posts</h1>
    <div class="posts">
      <div v-for="post in posts" :key="post.slug" class="post-card">
        <h2>{{ post.title }}</h2>
        <p class="date">{{ post.date }}</p>
        <p class="excerpt">{{ post.excerpt }}</p>
        <router-link :to="`/blog/${post.slug}`" class="read-more">Read More →</router-link>
      </div>
    </div>
    <div class="nav-links">
      <router-link to="/" class="btn-back">← Back to Home</router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// List of available blog posts
const posts = ref([
  {
    slug: 'welcome-post',
    title: 'Welcome to My Blog',
    date: '2024-01-01',
    excerpt: 'This is my first blog post. Learn about what this blog is all about.'
  },
  {
    slug: 'vue3-features',
    title: 'Exploring Vue 3 Features',
    date: '2024-01-15',
    excerpt: 'Dive into the exciting new features of Vue 3 and how they improve development.'
  },
  {
    slug: 'static-site-generation',
    title: 'Static Site Generation with Vue',
    date: '2024-02-01',
    excerpt: 'Learn how to build and deploy static sites using Vue 3 and Vite.'
  }
])
</script>

<style scoped>
.blog-list {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
}

h1 {
  text-align: center;
  color: #42b883;
  margin-bottom: 2rem;
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
  color: #333;
}

.date {
  color: #999;
  font-size: 0.9rem;
  margin: 0.5rem 0;
}

.excerpt {
  color: #666;
  line-height: 1.6;
}

.read-more {
  display: inline-block;
  margin-top: 1rem;
  color: #42b883;
  text-decoration: none;
  font-weight: 600;
}

.read-more:hover {
  color: #35a372;
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
