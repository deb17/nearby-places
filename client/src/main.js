import Vue from 'vue'
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import BootstrapVue from 'bootstrap-vue'
import App from './App.vue'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(BootstrapVue)

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyChbfEPil-9qN24P4HpjRM5H6s_DSId6t0'
  }
})

new Vue({
  el: '#app',
  render: h => h(App)
})
