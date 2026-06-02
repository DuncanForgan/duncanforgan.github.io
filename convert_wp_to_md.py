#!/usr/bin/env python3
"""
WordPress WXR to Markdown converter for duncanforgan.github.io.

Usage:
    pip install markdownify
    python convert_wp_to_md.py wordpress-export.xml

For each published post the script will:
  - Write a .md file to src/posts/{slug}.md
  - Print the blogPosts.js config entry to stdout

After running, copy the printed entries into src/config/blogPosts.js in
date order alongside any existing posts.
"""

import argparse
import re
import sys
import textwrap
import xml.etree.ElementTree as ET
from pathlib import Path

try:
    from markdownify import markdownify as md
except ImportError:
    sys.exit(
        "Error: markdownify is not installed.\n"
        "Run:  pip install markdownify\n"
        "then try again."
    )

# ---------------------------------------------------------------------------
# WordPress WXR XML namespaces
# ---------------------------------------------------------------------------
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "wp":      "http://wordpress.org/export/1.2/",
    "dc":      "http://purl.org/dc/elements/1.1/",
    "excerpt": "http://wordpress.org/export/1.2/excerpt/",
}

# Also try the older 1.1 namespace if items are missing
NS_ALT = {**NS, "wp": "http://wordpress.org/export/1.1/"}


def get_text(item: ET.Element, tag: str, namespaces: dict, default: str = "") -> str:
    el = item.find(tag, namespaces)
    return (el.text or "").strip() if el is not None else default


def slugify(text: str) -> str:
    """Convert arbitrary text to a URL/filename-safe slug."""
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def html_to_markdown(html: str) -> str:
    """Convert an HTML string to clean Markdown."""
    return md(
        html,
        heading_style="ATX",      # Use # style headings
        bullets="-",               # Use - for unordered lists
        newline_style="backslash", # Preserve intentional line breaks
        strip=["script", "style"],
    ).strip()


def extract_excerpt(markdown_body: str, max_chars: int = 150) -> str:
    """
    Generate a plain-text excerpt from the markdown body.
    Strips markdown syntax and truncates to max_chars.
    """
    # Remove headings
    text = re.sub(r"^#{1,6}\s+", "", markdown_body, flags=re.MULTILINE)
    # Remove emphasis/bold markers
    text = re.sub(r"[*_]{1,3}(.+?)[*_]{1,3}", r"\1", text)
    # Remove inline links, keep link text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    # Remove image syntax
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    # Collapse whitespace
    text = re.sub(r"\s+", " ", text).strip()

    if len(text) <= max_chars:
        return text

    # Truncate at a word boundary
    truncated = text[:max_chars].rsplit(" ", 1)[0]
    return truncated.rstrip(".,;:!?") + "..."


def parse_date(raw_date: str) -> str:
    """
    Return YYYY-MM-DD from a WordPress post date string like
    '2023-04-12 10:30:00' or fall back to the raw value.
    """
    match = re.match(r"(\d{4}-\d{2}-\d{2})", raw_date)
    return match.group(1) if match else raw_date


def iter_posts(root: ET.Element) -> list[dict]:
    """Extract all published posts from the WXR element tree."""
    posts = []
    namespaces = NS

    channel = root.find("channel")
    if channel is None:
        sys.exit("Error: could not find <channel> element in the export file.")

    for item in channel.findall("item"):
        post_type = get_text(item, "wp:post_type", namespaces)
        status    = get_text(item, "wp:status",    namespaces)

        # Retry with alternate namespace if both are empty
        if not post_type:
            post_type = get_text(item, "wp:post_type", NS_ALT)
            status    = get_text(item, "wp:status",    NS_ALT)
            namespaces = NS_ALT

        if post_type != "post" or status != "publish":
            continue

        title    = get_text(item, "title",              namespaces)
        raw_slug = get_text(item, "wp:post_name",       namespaces)
        raw_date = get_text(item, "wp:post_date",       namespaces)
        content  = get_text(item, "content:encoded",    namespaces)

        slug = raw_slug if raw_slug else slugify(title)
        date = parse_date(raw_date)

        posts.append({
            "slug":    slug,
            "title":   title,
            "date":    date,
            "content": content,
        })

    return posts


def write_markdown(post: dict, posts_dir: Path) -> Path:
    """Write a single post as a Markdown file and return the path."""
    body = html_to_markdown(post["content"])

    # Build the file content: # Title heading + blank line + body
    md_content = f"# {post['title']}\n\n{body}\n"

    out_path = posts_dir / f"{post['slug']}.md"
    out_path.write_text(md_content, encoding="utf-8")
    return out_path


def format_js_entry(post: dict, excerpt: str) -> str:
    """Return the blogPosts.js object literal for a single post."""
    # Escape single quotes in strings
    title   = post["title"].replace("'", "\\'")
    excerpt = excerpt.replace("'", "\\'")
    return textwrap.dedent(f"""\
      {{
        slug: '{post["slug"]}',
        title: '{title}',
        date: '{post["date"]}',
        excerpt: '{excerpt}'
      }}""")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a WordPress WXR export to Markdown files for duncanforgan.github.io."
    )
    parser.add_argument("wxr_file", help="Path to the WordPress export XML file")
    parser.add_argument(
        "--posts-dir",
        default=str(Path(__file__).parent / "src" / "posts"),
        help="Directory to write .md files into (default: src/posts/)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be done without writing any files",
    )
    args = parser.parse_args()

    wxr_path  = Path(args.wxr_file)
    posts_dir = Path(args.posts_dir)

    if not wxr_path.exists():
        sys.exit(f"Error: file not found: {wxr_path}")

    if not args.dry_run:
        posts_dir.mkdir(parents=True, exist_ok=True)

    print(f"Parsing {wxr_path} …\n")

    try:
        tree = ET.parse(wxr_path)
    except ET.ParseError as exc:
        sys.exit(f"Error: failed to parse XML: {exc}")

    posts = iter_posts(tree.getroot())

    if not posts:
        print("No published posts found in the export file.")
        return

    # Sort by date ascending so the printed JS entries are in order
    posts.sort(key=lambda p: p["date"])

    js_entries = []

    for post in posts:
        body    = html_to_markdown(post["content"])
        excerpt = extract_excerpt(body)

        if args.dry_run:
            print(f"[dry-run] Would write: {posts_dir / post['slug']}.md")
        else:
            out_path = write_markdown(post, posts_dir)
            print(f"Written:  {out_path}")

        js_entries.append(format_js_entry(post, excerpt))

    print(f"\n{'─' * 60}")
    print(f"Converted {len(posts)} post(s).")
    print()
    print("Add the following entries to src/config/blogPosts.js")
    print("(insert in date order alongside existing posts):")
    print(f"{'─' * 60}\n")

    for entry in js_entries:
        print(entry + ",")
        print()

    print("─" * 60)
    print()
    print("Next steps:")
    print("  1. Review the generated .md files in src/posts/")
    print("  2. Check for WordPress shortcodes (e.g. [gallery]) that need manual cleanup")
    print("  3. Decide whether to hotlink or locally host any images")
    print("  4. Copy the entries above into src/config/blogPosts.js")


if __name__ == "__main__":
    main()
