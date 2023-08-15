<template>
  <div>
    <h4>commentListItem</h4>
    <div v-if="isEdit === false">
      {{comment}}
      <button @click.prevent="commentUpdate">[EDIT]</button>
      <button @click.prevent="commentDelete">[DELETE]</button>
    </div>
    <div v-if="isEdit === true">
      <form @submit.prevent="commentUpdated">
        <input type="text" id="content" v-model="content">
        <input type="submit" value="수정하기">
      </form>
    </div>
  </div>
</template>

<script>
export default {
  name : 'CommentListItem',
  props: {
    comment: Object,
  },
  data() {
    return {
      isEdit : false,
      content : this.comment.content,
    }
  },
  methods: {
    commentDelete() {
      this.$store.dispatch('commentDelete', this.comment.id)
    },
    commentUpdate() {
      this.isEdit = true
      console.log(this.isEdit)
    },
    commentUpdated() {
      console.log(this.isEdit)
      const payload = {commentpk : this.comment.id, content : this.content, review : this.comment.review}
      this.$store.dispatch('commentUpdate', payload)
      this.isEdit = false
    }
  }
}
</script>

<style>

</style>