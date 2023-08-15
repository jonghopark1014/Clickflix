<template>
  <div>
    <h1>Famousline List</h1>
    <div v-if="famouslines !== {}">
      <FamousLineListItem
        v-for="famousline in famouslines" :key=famousline.id
        :famousline=famousline
      />
    </div>
    <div v-else>
      명대사 없다 
    </div>
  </div>
</template>

<script>
import FamousLineListItem from '@/components/famousline/FamousLineListItem'

export default {
  name : 'FamousLineList',
  components: {
    FamousLineListItem,
  },
  computed: {
    famouslines() {
      console.log(this.$store.getters.famouslines)
      return this.$store.getters.famouslines
    }
  },
  created() {
      this.$store.dispatch('getFamouslines')
  }
}
</script>

<style>

</style>