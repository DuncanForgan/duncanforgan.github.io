import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import BlogList from '../views/BlogList.vue'
import BlogPost from '../views/BlogPost.vue'
import AcademicResearch from '../views/AcademicResearch.vue'
import Writing from '../views/Writing.vue'
import SoftwareEngineering from '../views/SoftwareEngineering.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/blog',
      name: 'blog',
      component: BlogList
    },
    {
      path: '/blog/:slug',
      name: 'blog-post',
      component: BlogPost
    },
    {
      path: '/research',
      name: 'academic-research',
      component: AcademicResearch
    },
    {
      path: '/writing',
      name: 'writing',
      component: Writing
    },
    {
      path: '/software',
      name: 'software-engineering',
      component: SoftwareEngineering
    }
  ]
})

export default router
