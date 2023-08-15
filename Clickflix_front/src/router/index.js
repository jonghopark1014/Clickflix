import Vue from 'vue'
import VueRouter from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import NotFound404 from '@/views/NotFound404'
// movie
import MovieListView from '@/views/movie/MovieListView'
import MovieDetailView from '@/views/movie/MovieDetailView'
// recommend
import RecommendView from '@/views/recommend/RecommendView'
// community
import CommunityView from '@/views/community/CommunityView'
// // Review
import ReviewView from '@/views/community/ReviewView'
import ReviewDetailView from '@/views/community/ReviewDetailView'
import ReviewCreateView from '@/views/community/ReviewCreateView'
import ReviewUpdateView from '@/views/community/ReviewUpdateView'
// // Famousline
import FamousLineView from '@/views/community/FamousLineView'
import FamousLineCreateView from '@/views/community/FamousLineCreateView'
import FamousLineUpdateView from '@/views/community/FamousLineUpdateView'
// gotcha???
// import FamousLineView from '@/views/community/FamousLineView'
// user
import UserView from '@/views/user/UserView'
import UserInfoView from '@/views/user/UserInfoView'
import AnotherInfoView from '@/views/user/AnotherInfoView'

import LoSiview from '@/views/user/LoSiview'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/LoSiview',
    name: 'LoSiview',
    component: LoSiview
  },
  //movie
  {
    path: '/movielist',
    name: 'MovieList',
    component: MovieListView
  },
  {
    path: '/movie/:id',
    name: 'MovieDetail',
    component: MovieDetailView
  },
  // recommend
  {
    path: '/recommend',
    name: 'Recommend',
    component: RecommendView
  },
  // community
  {
    path: '/community',
    name: 'Community',
    component: CommunityView
  },
  // // Famousline
  {
    path: '/famousline',
    name: 'FamousLine',
    component: FamousLineView
  },
  {
    path : '/famousline/create',
    name : 'FamousLineCreate',
    component : FamousLineCreateView
  },
  {
    path : '/famousline/:id/update',
    name : 'FamousLineUpdate',
    component : FamousLineUpdateView
  },
  // // Review
  {
    path: '/review',
    name: 'ReviewView',
    component: ReviewView
  },
  {
    path: '/review/:id',
    name: 'ReviewDetail',
    component: ReviewDetailView
  },
  {
    path: '/review/create',
    name: 'ReviewCreate',
    component: ReviewCreateView
  },
  {
    path: '/review/:id/update',
    name: 'ReviewUpdate',
    component: ReviewUpdateView
  },
  // user
  {
    path: '/user',
    name: 'User',
    component: UserView
  },
  {
    path: '/userinfo/',
    name: 'UserInfo',
    component: UserInfoView
  },
  {
    path: '/user/info/:id/',
    name: 'AnotherInfo',
    component: AnotherInfoView
  },
  {
    path: '/404',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: '/404',
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
