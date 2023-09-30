import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import VueFullscreen from 'vue-fullscreen'
// 引入 router
import router from './router'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'

// 使用
const app = createApp(App)
app.use(router).use(VueFullscreen).use(ElementPlus).mount('#app')
