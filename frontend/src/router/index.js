import Vue from 'vue'
import Router from 'vue-router'
import Main from '@/components/Main'
import Training from '@/components/Training'
import Prediction from '@/components/Prediction'
import Statistics from '@/components/Statistics'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/train',
      name: 'Training',
      component: Training
    },
    {
      path: '/predict',
      name: 'Prediction',
      component: Prediction
    },
    {
      path: '/stats',
      name: 'Statistics',
      component: Statistics
    }
  ]
})
