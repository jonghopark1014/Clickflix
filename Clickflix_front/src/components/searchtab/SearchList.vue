<template>
  <div>
    <div class="container">
      <div class="row row-cols-3 row-cols-md-5">
        <SearchListItem v-for="searchitem in searchlist" :key=searchitem.id.id :searchitem=searchitem />
      </div>
    </div>
  </div>
</template>

<script>
import SearchListItem from '@/components/searchtab/SearchListItem'
export default {
  name: 'SearchList',
  components: {
    SearchListItem,
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