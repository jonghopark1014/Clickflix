<template>
  <div>
    <div v-if="reviews !== {}">
      <ReviewListItem v-for="review in reviews" :key=review.id :review=review />
    </div>
    <div v-else>
      리뷰가 존재하지 않습니다
    </div>
  </div>
</template>

<script>
import ReviewListItem from '@/components/review/ReviewListItem'
export default {
  name: 'ReviewList',
  components: {
    ReviewListItem
  },
  computed: {
    reviews() {
      return this.$store.state.reviews
    }
  }
}
</script>

<style>

</style>