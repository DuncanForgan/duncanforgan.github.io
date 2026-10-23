import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { readFile } from 'node:fs/promises'
import { parse } from 'yaml'
import { splitPost } from './src/config/postContent.js'

function postMetadata() {
  return {
    name: 'post-metadata',
    enforce: 'pre',
    async load(id) {
      const [filename, query] = id.split('?')
      if (!filename.endsWith('.md') || query !== 'metadata') return null

      this.addWatchFile(filename)
      const { frontMatter } = splitPost(await readFile(filename, 'utf8'))
      const metadata = parse(frontMatter)
      for (const field of ['title', 'date']) {
        if (typeof metadata?.[field] !== 'string' || !metadata[field].trim()) {
          this.error(`${filename}: ${field} must be a non-empty string`)
        }
        if (metadata.excerpt != null && typeof metadata.excerpt !== 'string') {
          this.error(`${filename}: excerpt must be a string`)
        }
      }
      const date = metadata.date
      if (!/^\d{4}-\d{2}-\d{2}$/.test(date) ||
          !Number.isFinite(Date.parse(date)) ||
          new Date(date).toISOString().slice(0, 10) !== date) {
        this.error(`${filename}: date must be a valid YYYY-MM-DD date`)
      }
      return `export default ${JSON.stringify({
        title: metadata.title,
        date,
        excerpt: metadata.excerpt ?? '',
      })}`
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [postMetadata(), vue()],
  assetsInclude: ['**/*.md'],
  base: '/',
})
