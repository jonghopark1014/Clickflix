<template>
  <div>
    <ReviewSearchBar />
    <ReviewSearchlist />
    <h3>{{ searchmovie.title }}</h3>
    <form @submit.prevent="UpdateReview">
      <label for="point">평점: </label>
      <input type="number" id="point" v-model.trim="point"><br>
      <label for="title">제목: </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용: </label>
      <input type="text" id="content" v-model.trim="content"><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import ReviewSearchBar from '@/components/review/ReviewSearchBar'
import ReviewSearchlist from '@/components/review/ReviewSearchlist'

export default {
  name: 'ReviewForm',
  props: {
    review : Object,
  },
  components: {
    ReviewSearchBar,
    ReviewSearchlist,
  },
  data() {
    return {
      title : this.review.title,
      point : this.review.point,
      content : this.review.content,
      movie: this.review.movie,
    }
  },
  computed: {
    searchmovie() {
      return this.$store.getters.searchmovie
    }
  },
  methods: {
    UpdateReview() {
      const payload = {reviewid : this.review.id, movieid : this.searchmovie.id, title: this.title, point : this.point, content : this.content}
      this.$store.dispatch('UpdateReview', payload)
      this.$store.state.searchmovie = ''
    }
  }

}
</script>

<style>

</style>