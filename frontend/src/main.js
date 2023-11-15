import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import VueFullscreen from 'vue-fullscreen'
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import axios from "axios";
import PerfectScrollbar from 'vue3-perfect-scrollbar'
import 'vue3-perfect-scrollbar/dist/vue3-perfect-scrollbar.css'
import * as ElementPlusIconsVue from '@element-plus/icons-vue'

const app = createApp(App)
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}
app.config.globalProperties.axios=axios //全局配置axios
app.use(router).use(VueFullscreen).use(ElementPlus).use(PerfectScrollbar).mount('#app')