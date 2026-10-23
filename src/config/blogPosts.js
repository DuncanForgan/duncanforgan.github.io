const metadata = import.meta.glob('../posts/*.md', {
  query: '?metadata',
  import: 'default',
  eager: true,
})

export const blogPosts = Object.entries(metadata)
  .map(([path, post]) => ({
    ...post,
    slug: path.slice('../posts/'.length, -'.md'.length),
  }))
  .sort((a, b) => b.date.localeCompare(a.date) || a.slug.localeCompare(b.slug))
