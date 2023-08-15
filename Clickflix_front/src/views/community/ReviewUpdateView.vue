<template>
  <div>
    <h4>Review Update View</h4>
    <ReviewForm
    :review="review"
     />
  </div>
</template>

<script>
import ReviewForm from '@/components/review/ReviewForm'

export default {
    name : 'ReviewUpdateView',
    components : {
        ReviewForm,
    },
    computed: {
        review() {
            return this.$store.getters.review
        }
    }
}
</script>

<style>

</style>