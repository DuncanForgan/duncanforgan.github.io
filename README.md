# DuncanForgan.github.io

A Vue 3 static website with blog functionality built using Vite.

## Features

- **Home Page**: Welcome page with navigation to blog
- **Blog List**: Page listing all available blog posts
- **Dynamic Blog Posts**: Markdown files rendered as blog posts using the `marked` library
- **Vue Router**: Dynamic routing for seamless navigation
- **Static Site Generation**: Built as a static site for easy deployment

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

Create a new markdown file in `src/posts/` and add it to the list in `src/views/BlogList.vue`.

## Deployment

The built static site can be deployed to any static hosting service like:
- GitHub Pages
- Netlify
- Vercel
- AWS S3

