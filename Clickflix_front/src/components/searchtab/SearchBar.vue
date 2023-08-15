<template>
  <div>
    <input type="text" style="width:500px" placeholder="검색어를 입력하세요 www" v-model.trim="searchMovie" @input="searching" @keyup.enter="searching">
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