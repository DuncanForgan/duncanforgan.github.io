// Ensures every markdown file in src/posts has an entry in src/config/blogPosts.js.
// Missing posts are added to the top of the list with today's date.
import { readFileSync, writeFileSync, readdirSync } from 'node:fs'
import { join, dirname } from 'node:path'
import { fileURLToPath, pathToFileURL } from 'node:url'

const root = join(dirname(fileURLToPath(import.meta.url)), '..')
const postsDir = join(root, 'src', 'posts')
const configPath = join(root, 'src', 'config', 'blogPosts.js')

const { blogPosts } = await import(pathToFileURL(configPath).href)
const existing = new Set(blogPosts.map((p) => p.slug))

const missing = readdirSync(postsDir)
  .filter((f) => f.endsWith('.md'))
  .map((f) => f.slice(0, -3))
  .filter((slug) => !existing.has(slug))
  .sort()

if (missing.length === 0) {
  console.log('blogPosts.js is up to date.')
  process.exit(0)
}

const today = new Date().toISOString().slice(0, 10)

const toPlainText = (md) =>
  md
    .replace(/!\[[^\]]*\]\([^)]*\)/g, '') // images
    .replace(/\[([^\]]*)\]\([^)]*\)/g, '$1') // links
    .replace(/<[^>]+>/g, '') // html tags
    .replace(/[*_`>#]/g, '')
    .replace(/\s+/g, ' ')
    .trim()

function buildEntry(slug) {
  const lines = readFileSync(join(postsDir, `${slug}.md`), 'utf8').split(/\r?\n/)
  const headingIndex = lines.findIndex((l) => /^#\s+/.test(l))
  const title = headingIndex >= 0
    ? lines[headingIndex].replace(/^#\s+/, '').trim()
    : slug.split('-').map((w) => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')

  const body = toPlainText(lines.filter((_, i) => i !== headingIndex).join('\n'))
  const excerpt = body.length > 150 ? `${body.slice(0, 150).replace(/\s+\S*$/, '')}...` : body

  return [
    '{',
    `  slug: ${JSON.stringify(slug)},`,
    '  tags: [],',
    `  title: ${JSON.stringify(title)},`,
    `  date: ${JSON.stringify(today)},`,
    `  excerpt: ${JSON.stringify(excerpt)}`,
    '},',
  ].join('\n')
}

const source = readFileSync(configPath, 'utf8')
const marker = /export const blogPosts = \[\s*\n/
if (!marker.test(source)) {
  console.error('Could not find "export const blogPosts = [" in blogPosts.js')
  process.exit(1)
}

const entries = missing.map(buildEntry).join('\n') + '\n'
writeFileSync(configPath, source.replace(marker, (m) => m + entries))

console.log(`Added ${missing.length} post(s) to blogPosts.js: ${missing.join(', ')}`)
