import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import BattleForm from '../views/BattleForm.vue'
import BattleList from '../views/BattleList.vue'
import BattleDetail from '@/components/BattleDetail.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/detail',
    name: 'detail',
    component: BattleDetail   
  },
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/battleform',
    name: 'battleform',
    component: BattleForm
  },
  {
    path: '/battlelist',
    name: 'battlelist',
    component: BattleList
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
