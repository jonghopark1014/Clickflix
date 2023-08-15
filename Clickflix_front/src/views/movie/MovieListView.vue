<template>
    <div class="userinfo_all">
    <div class="userinfo_profile-all">
    <div class="userinfo_apple">
    <div class="userinfo_header">
      <div class="userinfo_menu-circle"></div>
      <div class="userinfo_header-profile">
        <div>
          <h1>영화 목록</h1>
        </div>
      </div>
    </div>
    <!-- 바디 -->
    
    <div class="userinfo_wrapper">
      <div class="userinfo_main-container">
        <div class="userinfo_main-header">
          <div class="userinfo_header-menu">
          <SearchBar />
          <div style="height: 10px;">
          </div>
        </div>
      </div>
      <SearchList />
      </div>
    </div>
  </div>
  <div class="userinfo_overlay-app"></div>
</div>
</div>
</template>

<script>
import {mapState} from 'vuex'
import SearchBar from '@/components/searchtab/SearchBar'
// import MovieList from '@/components/movie/MovieList'
import SearchList from '@/components/searchtab/SearchList.vue'

export default {
  name: 'MovieListView',
  components: {
    SearchBar,
    // MovieList,
    SearchList,
  },
  computed: {
    ...mapState([
      "searchword"
    ])
  },
  created() {
    this.$store.dispatch('searching', '')
  }
}
</script>

<style>

</style>