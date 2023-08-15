<template>
  <div>
    {{ searchitem.title }}
    <button @click="reviewpick">선택</button>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ReviewSearchItem',
  props: {
    searchitem: Object
  },
  methods: {
    reviewpick() {
      // console.log(this.searchitem)
      this.$store.dispatch('reviewpick', this.searchitem)
      this.$store.state.searchlist = null
    }
  }
}
</script>

<style>

</style>