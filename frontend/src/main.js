import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import VueFullscreen from 'vue-fullscreen'
// 引入 router
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";
import PerfectScrollbar from 'vue3-perfect-scrollbar'
import 'vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css'
// 使用
const app = createApp(App)
app.config.globalProperties.axios=axios //全局配置axios
app.use(router).use(VueFullscreen).use(ElementPlus).use(PerfectScrollbar).mount('#app')
