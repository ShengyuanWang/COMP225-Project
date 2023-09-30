import {createRouter, createWebHistory} from 'vue-router'

const routerHistory = createWebHistory()

import Vindex from './views/index/Vindex.vue'
import Vsearch from './views/search/Vsearch.vue'
import Vtest from './views/test/Vtest.vue'
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
        path: '/test',
        name: 'Vtest',
        component: Vtest
    },
]

// 创建路由器
const router = createRouter({
    history: routerHistory,
    routes: routes
})


export default router;
