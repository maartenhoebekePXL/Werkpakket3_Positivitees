import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import EmptyStateView from '../views/EmptyStateView.vue' // Import EmptyStateView

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/EmptyStateView',
      name: 'EmptyStateView',
      component: EmptyStateView // Use EmptyStateView component
    }
  ]
})

export default router
