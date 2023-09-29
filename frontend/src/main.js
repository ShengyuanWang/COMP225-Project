import './assets/main.css'

import {createApp} from 'vue'
import App from './App.vue'
import VueFullscreen from 'vue-fullscreen'
// 引入 router
import router from './router'

// 使用
const app = createApp(App)
app.use(router).use(VueFullscreen).mount('#app')
