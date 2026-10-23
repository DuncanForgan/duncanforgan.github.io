# DuncanForgan.github.io

A Vue 3 static website with blog functionality built using Vite.

## Features

- **Home Page**: Welcome page with navigation to blog
- **Blog List**: Page listing all available blog posts
- **Dynamic Blog Posts**: Markdown files rendered as blog posts using the `marked` library
- **Vue Router**: Dynamic routing for seamless navigation
- **Static Site Generation**: Built as a static site for easy deployment
- **Mobile Publishing**: Decap CMS at `/admin/` with drafts, Markdown/rich-text editing, and image uploads

## Tech Stack

- **Vue 3**: Progressive JavaScript framework
- **Vite**: Next generation frontend tooling
- **Vue Router**: Official router for Vue.js
- **Marked**: Markdown parser and compiler

## Development

Install dependencies:
```bash
npm install
```

Run development server:
```bash
npm run dev
```

Build for production:
```bash
npm run build
```

Preview production build:
```bash
npm run preview
```

## Project Structure

```
src/
├── assets/         # Static assets
├── components/     # Vue components
├── posts/          # Markdown blog posts
├── router/         # Vue Router configuration
├── views/          # Page components
│   ├── Home.vue
│   ├── BlogList.vue
│   └── BlogPost.vue
├── App.vue         # Root component
└── main.js         # Application entry point
```

## Adding Blog Posts

### From an iPhone

After the one-time authentication setup below:

1. Open `https://duncanforgan.github.io/admin/` in Safari and log in with GitHub.
   The account needs write access to this repository. You can bookmark the editor
   or add it to your Home Screen.
2. Select **Blog posts → New Blog post**, enter a title, date, and optional excerpt,
   then write or dictate the body. Use the Markdown widget's rich-text mode if
   you prefer not to type Markdown. There is no need to repeat the title in the body.
3. Use the image control to upload from your photo library. Images are committed
   under `public/images/uploads/` and referenced as `/images/uploads/...`.
4. Save a draft, then move it through the editorial workflow and publish when ready.
   Decap manages the draft branch and pull request; you do not need to create files
   or update a separate list. Save before leaving Safari; do not rely on unsaved
   browser state, and use an internet connection for saving and publishing.
5. Publishing merges into `main`, triggering the existing GitHub Pages deployment.
   Wait for that workflow to finish before checking the public blog.

The preview pane shows the body, not a complete deployment of the site. On a
narrow screen you may need to switch between editing and preview. Draft branches
and PRs in this **public repository are public**, even though drafts are not
included in the deployed blog.

### One-time authentication setup (repository owner)

GitHub Pages cannot hold an OAuth client secret or run the OAuth exchange.
The editor therefore uses Decap's GitHub backend with Netlify's hosted OAuth
service. **Authentication is not ready until you complete these steps.**
The actual website and DNS remain on GitHub Pages; Netlify is used only for OAuth.

1. Create a Netlify project (a placeholder deployment is sufficient) and record its
   `your-project.netlify.app` hostname.
2. In GitHub **Settings → Developer settings → OAuth Apps**, register an app:
   - Homepage URL: `https://duncanforgan.github.io`
   - Authorization callback URL: `https://api.netlify.com/auth/done`
3. In that Netlify project's OAuth/authentication-provider settings, configure
   GitHub with the app's client ID and client secret. These are OAuth provider
   settings, not Netlify Identity or Git Gateway.
4. Replace `REPLACE-ME.netlify.app` in `public/admin/config.yml` with the Netlify
   project hostname, without `https://` or a path, and deploy the change.
   `site_domain` identifies the authentication project, not the blog's domain.
5. On the deployed HTTPS `/admin/` page, test login, saving a draft, and publishing.
   Confirm that the draft stays off the public blog and that publishing triggers
   Pages. GitHub login does not grant repository write permissions by itself.

Only public OAuth configuration belongs in the repository. **Never put a client
secret or GitHub access token in the CMS config, site JavaScript, or Markdown.**
The configured `public_repo` scope avoids requesting private repository access,
but is not restricted to this one public repository. Use a trusted OAuth provider.
The CMS release is pinned and its CDN script is checked using Subresource Integrity.
If upgrading it, update both the version and integrity hash.

The default `editorial_workflow` keeps drafts on branches and lets the CMS publish
by merging PRs. GitHub branch protections still apply: required reviews/checks may
need to be satisfied in GitHub before publication; do not weaken those protections
just to bypass the workflow. If you intentionally want immediate publishing,
remove `publish_mode: editorial_workflow` from the config. This loses branch-based
drafts and requires permission to push directly to `main`.

See [Decap's GitHub backend](https://decapcms.org/docs/github-backend/) and
[authentication options](https://decapcms.org/docs/authentication-backends/)
for configuration details and alternatives to Netlify's OAuth service.

### From a local editor

Create `src/posts/your-post-slug.md` with YAML front matter:

```markdown
---
title: "My new post"
date: "2026-10-23"
excerpt: "A short description for the blog listing."
---

Write the post here.
```

The filename determines `/blog/your-post-slug`; keep existing filenames unchanged
to preserve links. Title and date are required, and date must be `YYYY-MM-DD`.
Excerpt is optional. Vite discovers posts and builds the date-sorted listing from
their front matter automatically, without shipping the YAML parser to browsers.
Front matter is stripped before rendering. Existing body headings are preserved;
otherwise the title field supplies the page heading. Post HTML is sanitized.

`convert_wp_to_md.py` also writes this format when importing WordPress posts;
there is no longer a separate JavaScript metadata file to paste into.

## Deployment

The built static site can be deployed to any static hosting service like:
- GitHub Pages
- Netlify
- Vercel
- AWS S3
