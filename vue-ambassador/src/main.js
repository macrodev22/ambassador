import { createApp } from 'vue'
import { createPinia } from 'pinia'
import '../node_modules/bootstrap/scss/bootstrap.scss'
import './style.css'
import App from './App.vue'
import router from './router'

const pinia = createPinia()

createApp(App)
.use(router)
.use(pinia)
.mount('#app')
