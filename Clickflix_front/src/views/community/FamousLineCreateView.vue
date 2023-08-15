<template>
  <div>
    <h4>Create FamousLine</h4>
    <ReviewSearchBar />
    <ReviewSearchlist />
    <h3>{{ searchmovie.title}}</h3>
    <form @submit.prevent="createFamousline">
      <label for="content">대사: </label>
      <input type="text" id="content" v-model="content"><br>
      <label for="speaker">이름: </label>
      <input type="text" id="speaker" v-model="speaker"><br>
      <input type="submit" id="submit">
    </form>

  </div>
</template>

<script>
import ReviewSearchBar from '@/components/review/ReviewSearchBar'
import ReviewSearchlist from '@/components/review/ReviewSearchlist'

export default {
  name : 'FamousLineCreateView',
  components : {
    ReviewSearchBar,
    ReviewSearchlist,
  },
  computed: {
    searchmovie() {
      return this.$store.getters.searchmovie
    },
  },
  data() {
    return {
      content : null,
      speaker: null,
    }
  },
  methods: {
    createFamousline() {
      const payload = {movieid: this.searchmovie.id, content : this.content, speaker : this.speaker,}
      this.$store.dispatch('createFamousline', payload)
      this.$store.state.searchmovie = ''
    },
  }
}
</script>

<style>

</style>