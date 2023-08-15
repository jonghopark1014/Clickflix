<template>
  <div>
    <h1>영화 리스트</h1>
    <div class="container">
      <div class="row row-cols-3 row-cols-md-5">
        <MovieListItem v-for="movie in listall" :key=movie.id :movie=movie />
      </div>
    </div>
  </div>
</template>

<script>
import MovieListItem from '@/components/movie/MovieListItem'
export default {
  name: 'MovieList',
  components: {
    MovieListItem,
  },
  computed: {
    listall() {
      return this.$store.getters.listall
    }
  }
}
</script>

<style>

</style>