import Vue from 'vue';
import VueRouter from 'vue-router';
import Books from '../components/Books.vue';
import Ping from '../components/Ping.vue';

Vue.use(VueRouter);

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'Books',
      component: Books,
    },
    {
      path: '/ping',
      name: 'Ping',
      component: Ping,
    },
  ],
});

export default router;
