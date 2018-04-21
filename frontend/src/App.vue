<template>
  <div id="app">
    <b-navbar type="dark" variant="info" toggleable>
      <b-navbar-nav>
        <b-nav-item class="nav-item" to="/">Home</b-nav-item>
        <b-nav-item class="nav-item" to="/train">Train</b-nav-item>
        <b-nav-item class="nav-item" to="/predict">Predict</b-nav-item>
        <b-nav-item class="nav-item" to="/stats">Statistics</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    <router-view/>
    <div d-flex justife-content-center class="footer">
      <a href="https://github.com/bszelag/breast-cancer-classification">
        <font-awesome-icon class="github" :icon="github"/>
      </a>
    </div>
  </div>
</template>

<script>
import axios from '../node_modules/axios'
import Vue from 'vue'
import FontAwesomeIcon from '../node_modules/@fortawesome/vue-fontawesome'
import { faGithub } from '../node_modules/@fortawesome/fontawesome-free-brands'

const BACKEND_URL = process.env.BACKEND_URL || 'http://127.0.0.1'
const BACKEND_PORT = process.env.BACKEND_PORT || '5000'
Vue.prototype.$http = axios.create({
  baseURL: BACKEND_URL + ':' + BACKEND_PORT,
  headers: {'Content-type': 'application/json'}
})

export default {
  name: 'App',
  components: {
    // eslint-disable-next-line
    FontAwesomeIcon
  },
  computed: {
    github () {
      return faGithub
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-bottom: 60px;
}
.nav-item {
 margin: 5px;
}
.github {
  font-size: 1.5em;
}
.github:hover {
  cursor: pointer;
  color: #17a2b8;
}
.footer {
  bottom: 0px;
  position: fixed;
  padding: 1rem;
  left: 0px;
  right: 0px;
}
</style>
