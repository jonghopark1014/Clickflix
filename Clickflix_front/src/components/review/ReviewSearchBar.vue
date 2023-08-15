<template>
  <div>
    <span>영화를 검색하세요</span> | 
    <input type="text" placeholder="검색어를 입력하세요" v-model.trim="searchMovie" @input="searching" @keyup.enter="searching"><br>
  </div>
</template>

<script>
// import router from '@/router'
export default {
  name: 'SearchBar',
  data() {
    return {
        searchMovie: '',
    }
  },
  methods: {
    searching(event) {
      this.searchMovie = event.target.value
      this.$store.dispatch('searching', this.searchMovie)
    },
    // searching(event) {
    //   this.searchMovie = event.target.value
    //     if (this.searchMovie !== '') {
    //         router.push({ name: 'MovieList', params: { name: this.searchMovie } })
    //     }
    // },
  }
}
</script>

<style>

</style>