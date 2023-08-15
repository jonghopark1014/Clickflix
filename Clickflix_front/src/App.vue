<template>
  <div id="app">
    <div v-if="$route.name !== 'NotFound404'" class="navbar-expand-md" >
      <div class="container">
        <div class="collapse navbar-collapse" id="navcol-1">
          <ul class="nav navbar-nav flex-grow-1 justify-content-evenly">
            <li class="nav-item" role="presentation"><router-link class="nav-link" :to="{ name: 'home' }"><b>CLICKFLIX</b></router-link></li>
            <li class="nav-item" role="presentation"><router-link @click.native="clearword" class="nav-link" :to="{ name: 'MovieList' }">Search</router-link></li>
            <li class="nav-item" role="presentation"><router-link @click.native="clearword" class="nav-link" :to="{ name: 'Recommend' }">Recommend</router-link></li>
            <li class="nav-item" role="presentation"><router-link @click.native="clearword" class="nav-link" :to="{ name: 'Community' }">Community</router-link></li>
            <li v-if="!isLogin" class="nav-item" role="presentation"><router-link v-if="!isLogin" class="nav-link" :to="{ name: 'LoSiview' }">Login</router-link></li>
            <li v-if="isLogin" class="nav-item" role="presentation"><router-link class="nav-link" :to="{ name: 'UserInfo' }">User</router-link></li>
            <li v-if="isLogin" class="nav-item" role="presentation"><a class="nav-link" @click="logout">Logout</a></li>
          </ul>
        </div>
      </div>
    </div>
    <router-view/>
  </div>
</template>

<script>
  export default {
    computed: {
      isLogin() { return this.$store.getters.isLogin }
    },
    methods: {
      logout() {this.$store.dispatch('logout')},
      clearword() {
        this.$store.state.searchword = ''
      }
    }
  }

  // =========================================================


</script>

<style>
* {
  font-family: 'Noto Sans KR', sans-serif;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 100%;
  margin: auto;
}

nav {
  background: linear-gradient(rgba(232,232,232,1), rgba(237,236,236,0.7864583134651184));
  /* background: linear-gradient(rgba(0,0,0,1), rgba(119,117,117,0.5307061672210693)); */
  /* width: 100%;
  width: 100%;
  overflow: hidden;
  height: 50px;
  opacity: 1;
  top: 0px;
  left: 0px; */
}
</style>
