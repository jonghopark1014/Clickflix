<template>
  <div>
    <div class="userinfo_content-section">
        <ul>
          <li class="userinfo_adobe-product">
          <div class="userinfo_products">
            {{review.movie}}
          </div>
          <span class="userinfo_status"><span class="userinfo_green"></span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{review.point}}점</span>
          <span @click="getLike" v-if="islike === false">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;좋아요 ♡</span>
          <span @click="getLike" v-if="islike === true">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;좋아요 ❤️</span>
          <span class="userinfo_status"><span class="userinfo_green"></span>&nbsp;&nbsp;{{islikecount}}</span>
          <router-link :to="{ name: 'ReviewDetail', params: { id: review.id } }">detail</router-link>
          <span class="userinfo_status" style="text-overflow: ellipsis;overflow: hidden;"><span class="userinfo_green"></span>{{review.title}}</span>
          </li>
        </ul>
      </div>
    

  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  },
  computed: {
    reviewitem() {
      return this.$store.getters.review
    },
    user() {
      return this.$store.getters.user
    },
    islike() {
      const value = this.review.like_users.includes(this.user.id) ? true : false;
      return value
    },
    islikecount() {
      return this.review.like_users.length
    }
  },
  methods: {
    getLike() {
      const review_id = this.review.id
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user) {
        axios({
          url : `${API_URL}/api/v1/community/review/${review_id}/like/`,
          method : 'post',
          headers : this.$store.getters.authHead,
        })
          .then(() => {
          this.$store.dispatch('getReviews')
        }) .catch((err) => console.log(err))
      }
    }
  },
  created() {
    this.$store.dispatch('getReviews')
    this.$store.dispatch('getUserInfo')
  },
}

</script>

<style>

</style>