<template>
  <div>
    <h1>리뷰</h1>
    <router-link :to="{ name: 'ReviewCreate' }">리뷰 쓰기</router-link>
    <ReviewList />
    <!-- <router-link :to="{ name: 'ReviewCreate' }">reviewcreate</router-link> -->
  </div>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'
export default {
  name: 'ReviewView',
  components: {
    ReviewList,
  },
  created() {
    this.$store.dispatch('getReviews')
  }
}
</script>

<style>

</style>