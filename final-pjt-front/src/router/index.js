import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import ShihTzuView from '@/views/ShihTzuView.vue'
import RankingView from '@/views/RankingView.vue'
import SearchView from '@/views/SearchView.vue'
import CinemaView from '@/views/CinemaView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'
import FollowerView from '@/views/FollowerView.vue'
import FollowingView from '@/views/FollowingView.vue'
import ProfileCommentsView from '@/views/ProfileCommentsView.vue'
import CollectionView from '@/views/CollectionView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/shihTzu',
      name: 'shihTzu',
      component: ShihTzuView
    },
    {
      path: '/ranking',
      name: 'ranking',
      component: RankingView
    },
    {
      path: '/search',
      name: 'search',
      component: SearchView
    },
    {
      path: '/cinema',
      name: 'cinema',
      component: CinemaView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/profile/:username',
      name: 'profile',
      component: ProfileView,
      children: [
        {
          path: 'follower',
          name: 'follower',
          component: FollowerView
        },
        {
          path: 'following',
          name: 'following',
          component: FollowingView
        },
        {
          path: 'comments',
          name: 'profilecomments',
          component: ProfileCommentsView
        },
        {
          path: 'collection',
          name: 'collection',
          component: CollectionView
        },
        {
          path: 'update',
          name: 'update',
          component: ProfileUpdateView
        },
      ]
    },
  ]
})

router.afterEach(() => {
  window.scrollTo(0, 0); // 페이지 최상단으로 스크롤
});

router.beforeEach((to, from, next) => {
  const publicPages = ['/', '/login', '/register']
  const authRequired = !publicPages.includes(to.path)
  const loggedIn = localStorage.getItem('token')

  if (authRequired && !loggedIn) {
    alert('로그인이 필요한 서비스입니다.')
    return next('/login')
  }

  next()
})

export default router
