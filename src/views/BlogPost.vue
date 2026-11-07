<template>
  <div class="blog">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <article v-else class="post-content">
      <header class="post-header">
        <h1 v-html="renderedTitle"></h1>
        <div class="author-details">
          <img :src="avatar" alt="Duncan Forgan" class="author-avatar">
          <div class="author-byline">
            <span class="author-name">Duncan Forgan</span>
            <time v-if="postMetadata?.date" :datetime="postMetadata.date">{{ formattedPostDate }}</time>
          </div>
        </div>
      </header>
      <!-- Note: v-html is used here to render markdown. Since markdown files are -->
      <!-- part of the repository and not user-generated, this is safe. -->
      <div v-html="renderedContent" class="markdown-content"></div>
      <div class="nav-links">
        <router-link to="/blog" class="btn-back">← Back to Blog List</router-link>
      </div>
    </article>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { marked } from 'marked'
import { blogPosts } from '../config/blogPosts'
import avatar from '../assets/Elevate-1521-crop.png'

const route = useRoute()
const loading = ref(true)
const error = ref(null)
const markdownContent = ref('')
const postTitle = ref('')
const postMetadata = computed(() => blogPosts.find(post => post.slug === route.params.slug))
const renderedTitle = computed(() => marked.parseInline(postTitle.value))
const formattedPostDate = computed(() => {
  if (!postMetadata.value?.date) return ''

  return new Intl.DateTimeFormat(undefined, {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(new Date(`${postMetadata.value.date}T00:00:00`))
})

const renderedContent = computed(() => {
  if (markdownContent.value) {
    const contentWithoutTitle = markdownContent.value.replace(/^#\s+.+(?:\r?\n|$)/m, '')
    return marked(contentWithoutTitle)
  }
  return ''
})

onMounted(async () => {
  const slug = route.params.slug
  try {
    // Import the markdown file dynamically
    const module = await import(`../posts/${slug}.md?raw`)
    const content = module.default
    
    // Extract title from first H1 heading if present
    const titleMatch = content.match(/^#\s+(.+)$/m)
    if (titleMatch) {
      postTitle.value = titleMatch[1]
    } else {
      postTitle.value = slug.split('-').map(word => 
        word.charAt(0).toUpperCase() + word.slice(1)
      ).join(' ')
    }
    
    markdownContent.value = content
    loading.value = false
  } catch (err) {
    error.value = `Post not found: ${slug}`
    loading.value = false
    console.error('Error loading post:', err)
  }
})
</script>

<style scoped>
.post-content {
  max-width: 680px;
  margin: 0 auto;
  padding: 1rem 0 2rem;
  text-align: left;
}

.post-header {
  margin-bottom: 2.5rem;
}

.post-header h1 {
  color: var(--text-color-light);
  font-size: clamp(2rem, 5vw, 3rem);
  line-height: 1.15;
  margin: 0 0 1.5rem;
  padding: 0;
  text-align: left;
}

.author-details {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.author-avatar {
  width: 48px;
  height: 48px;
  border-radius: 50%;
  object-fit: cover;
}

.author-byline {
  display: flex;
  flex-direction: column;
  line-height: 1.4;
}

.author-name {
  font-weight: 700;
}

.author-byline time {
  font-size: 0.9rem;
  opacity: 0.75;
}

.loading, .error {
  text-align: center;
  padding: 2rem;
  font-size: 1.2rem;
}

.error {
  color: var(--error-color);
}

.markdown-content {
  line-height: 1.8;
  color: var(--text-color-light);
  overflow-wrap: anywhere;
}

.markdown-content :deep(h1),
.markdown-content :deep(h2),
.markdown-content :deep(h3) {
  color: var(--text-color-light);
  margin-top: 2rem;
  margin-bottom: 1rem;
  text-align: left;
}

.markdown-content :deep(h2) {
  border-bottom: 1px solid currentColor;
  padding-bottom: 0.3rem;
}

.markdown-content :deep(p) {
  margin-bottom: 1rem;
}

.markdown-content :deep(img) {
  max-width: 100%;
  height: auto;
  display: block;
  margin: 1rem auto;
}

.markdown-content :deep(code) {
  background-color: #f5f5f5;
  padding: 0.2rem 0.4rem;
  border-radius: 3px;
  font-family: monospace;
}

.markdown-content :deep(pre) {
  background-color: #f5f5f5;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
}

.markdown-content :deep(pre code) {
  background-color: transparent;
  padding: 0;
}

.markdown-content :deep(a) {
  color: var(--link-color);
  text-decoration: none;
}

.markdown-content :deep(a:hover) {
  text-decoration: underline;
}

.markdown-content :deep(ul),
.markdown-content :deep(ol) {
  margin-bottom: 1rem;
  padding-left: 2rem;
}

.markdown-content :deep(blockquote) {
  border-left: 4px solid var(--text-color);
  padding-left: 1rem;
  margin-left: 0;  
  font-style: italic;
}

.nav-links {
  margin-top: 3rem;
  padding-top: 2rem;  
}

.btn-back {
  display: inline-block;
  padding: 0.75rem 1.5rem;    
  text-decoration: none;
  color: var(--text-color);
  background-color: var(--theme-primary);
  border-radius: 4px;
  transition: background-color 0.3s;
}

.btn-back:hover {
  background-color: #e0e0e0;
}

@media (prefers-color-scheme: dark) {
 .post-header h1,
 .markdown-content,
 .markdown-content :deep(h1),
 .markdown-content :deep(h2),
 .markdown-content :deep(h3) {
    color: var(--text-color-dark);        
  }

}

</style>
