export function splitPost(source) {
  const match = source.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/)
  if (!match) throw new Error('Post is missing YAML front matter')
  return { frontMatter: match[1], body: source.slice(match[0].length) }
}
