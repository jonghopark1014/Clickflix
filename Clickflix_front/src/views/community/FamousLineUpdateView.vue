<template>
  <div>
    <h4>FamousLine Update</h4>
    <FamousLineForm
      :famousline='famousline'
    />

  </div>
</template>

<script>
import FamousLineForm from '@/components/famousline/FamousLineForm.vue'

export default {
  name: 'FamousLineUpdate',
  components : {
    FamousLineForm,
  },
  computed: {
    famousline() {
      console.log(11)
      return this.$store.getters.famousline
    },
  },
  created() {
    this.$store.dispatch('getFamousline', this.$route.params.id)
    console.log(this.$route.params.id)
  }
}

</script>

<style>

</style>