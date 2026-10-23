<template>
  <div class="blog">
    <div v-if="loading" class="loading">Loading...</div>
    <div v-else-if="error" class="error">{{ error }}</div>
    <div v-else class="post-content">
      <h1 v-if="!hasHeading">{{ postTitle }}</h1>
      <div v-html="renderedContent" class="markdown-content"></div>
      <div class="nav-links">
        <router-link to="/blog" class="btn-back">← Back to Blog List</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import { marked } from 'marked'
import DOMPurify from 'dompurify'
import { blogPosts } from '../config/blogPosts'
import { splitPost } from '../config/postContent'

const route = useRoute()
const loading = ref(true)
const error = ref(null)
const markdownContent = ref('')
const postTitle = ref('')
const hasHeading = computed(() => /^#\s+.+$/m.test(markdownContent.value))
const posts = import.meta.glob('../posts/*.md', { query: '?raw', import: 'default' })

const renderedContent = computed(() => {
  if (markdownContent.value) {
    return DOMPurify.sanitize(marked(markdownContent.value))
  }
  return ''
})

watch(() => route.params.slug, async (slug, previousSlug, onCleanup) => {
  let cancelled = false
  onCleanup(() => { cancelled = true })
  loading.value = true
  error.value = null
  markdownContent.value = ''
  try {
    const post = blogPosts.find(post => post.slug === slug)
    const load = posts[`../posts/${slug}.md`]
    if (!post || !load) throw new Error('Post not found')
    const content = await load()
    if (cancelled) return
    postTitle.value = post.title
    markdownContent.value = splitPost(content).body
    loading.value = false
  } catch (err) {
    if (cancelled) return
    error.value = `Post not found: ${slug}`
    loading.value = false
    console.error('Error loading post:', err)
  }
}, { immediate: true })
</script>

<style scoped>
.blog-post {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
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
}

.markdown-content :deep(h2) {
  border-bottom: 1px solid #e0e0e0;
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
  color: --var(--link-color);
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
 .markdown-content,
 .markdown-content :deep(h1),
 .markdown-content :deep(h2),
 .markdown-content :deep(h3) {
    color: var(--text-color-dark);        
  }

  markdown-content :deep(blockquote) {
  border-left: 4px solid var(--text-color--dark);
  padding-left: 1rem;
  margin-left: 0;  
  font-style: italic;
}
}

</style>
