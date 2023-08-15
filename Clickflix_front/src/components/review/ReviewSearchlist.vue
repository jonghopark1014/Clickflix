<template>
  <div>
    <ReviewSearchItem v-for="searchitem in searchlist" :key=searchitem.id.id :searchitem=searchitem />
  </div>
</template>

<script>
import ReviewSearchItem from '@/components/review/ReviewSearchItem'
export default {
  name: 'ReviewSearchlist',
  components: {
    ReviewSearchItem,
  },
  computed: {
    searchlist() {
      return this.$store.state.searchlist
    }
  }
}
</script>

<style>

</style>