<template>
  <div>
    <h1>FamousLineListItem</h1>
    <p>명대사 나온 영화 : {{famousline.movie}}</p>
    <p>명대사 : {{famousline.content}}</p>
    <p>명대사 날린 인물 : {{famousline.speaker}}</p>
    <router-link :to="{name:'FamousLineUpdate', params: {id: famousline.id} }">[Update]</router-link>
    <button @click="famouslinedelete">[DELETE]</button>
  </div>
</template>

<script>
export default {
  name : 'FamousLineListItem',
  props : {
    famousline : Object,
  },
  methods: {
    famouslinedelete() {
      this.$store.dispatch('famouslineDelete', this.famousline.id)
    }
  }
}
</script>

<style>

</style>