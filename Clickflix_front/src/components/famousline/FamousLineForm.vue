<template>
  <div>
    <h3>{{ movie }}</h3>
    <form @submit.prevent="updateFamousline">
      <label for="content">대사: </label>
      <input type="text" id="content" v-model="content"><br>
      <label for="speaker">이름: </label>
      <input type="text" id="speaker" v-model="speaker"><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
export default {
  name : 'FamousLineForm',
  props: {
    famousline:Object,
  },
  computed: {
    searchmovie() {
      return this.$store.getters.searchmovie
    },
  },
  data() {
    return {
      content : this.famousline.content,
      speaker: this.famousline.speaker,
      movie : this.famousline.movie,
      famouslineid : this.famousline.id
    }
  },
  methods: {
    updateFamousline() {
      const payload = {movieid: this.movie, content : this.content, speaker : this.speaker, famouslineid : this.famouslineid}
      this.$store.dispatch('updateFamousline', payload)
      this.$store.state.searchmovie = ''
    },
  }
}
</script>

<style>

</style>