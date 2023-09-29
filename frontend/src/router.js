import {createRouter, createWebHistory} from 'vue-router'

const routerHistory = createWebHistory()

import Vindex from './views/index/Vindex.vue'
import Vsearch from './views/search/Vsearch.vue'
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
]

// 创建路由器
const router = createRouter({
    history: routerHistory,
    routes: routes
})


export default router;
