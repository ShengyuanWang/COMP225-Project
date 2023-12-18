import {createRouter, createWebHistory} from 'vue-router'

const routerHistory = createWebHistory()

import Vindex from './views/index/Vindex.vue'
import Vsearch from './views/search/Vsearch.vue'
import Vshow from './views/show/Vshow.vue'
import Vmatch from "@/views/match/Vmatch.vue";
import Vdetail from "@/views/detail/Vdetail.vue";
import Vtest from "@/views/test/Vtest.vue";
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
        name: 'Vmatch'
    },
    {
        path: "/detail",
        component: Vdetail,
        name: 'Vdetail'
    },
    {
        path: "/about",
        component: Vtest,
        name: 'Vtest'
    }

]


// 创建路由器
const router = createRouter({
    history: routerHistory,
    routes: routes
})


export default router;
