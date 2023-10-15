import {createRouter, createWebHistory} from 'vue-router'

const routerHistory = createWebHistory()

import Vindex from './views/index/Vindex.vue'
import Vsearch from './views/search/Vsearch.vue'
import Vshow from './views/show/Vshow.vue'
import Vmatch from "@/views/match/Vmatch.vue";
// 定义路由
const routes = [
    {
        path: '/',
        name: 'Vindex',
        component: Vindex
    },
    {
        path: '/search',
        name: 'Vsearch',
        component: Vsearch
    },
    {
        path: '/show',
        name: 'Vshow',
        component: Vshow
    },
    {
        path: "/match",
        component: Vmatch,
        name: Vmatch
    }

]


// 创建路由器
const router = createRouter({
    history: routerHistory,
    routes: routes
})


export default router;
