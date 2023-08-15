<template>
  <!-- <div>
    <h1>ReviewDetail</h1>
    <div v-if="review">
      <router-link :to="{name : 'AnotherInfo', params : {id : review.user.id}}"> {{review.user.nickname}} </router-link>
    </div>
    {{ review }}
    <br>
    <span>{{islikecount}}</span>
    
    <span @click="getLike" v-if="islike === false">♡</span>
    <span @click="getLike" v-if="islike === true">❤️</span>

  </div> -->

  <div class="info-text-left userinfo_all">
    <div class="userinfo_profile-all">
    <div class="userinfo_apple">
    <div class="userinfo_header">
      <div class="userinfo_menu-circle"></div>
      <div class="userinfo_header-profile">
        <div> </div>
      </div>
    </div>
    <!-- 바디 -->
    <div class="userinfo_wrapper">
      <div class="userinfo_main-container">
      <div class="userinfo_main-header">
        <div class="userinfo_header-menu">
        </div>
      </div>
      <div class="userinfo_content-wrapper">
        <div class="userinfo_content-section">
        <div class="userinfo_content-section-title"><h3>{{review.title}}</h3>       <h5><span>{{islikecount}}</span>
        <span @click="getLike" v-if="islike === false">♡</span>
        <span @click="getLike" v-if="islike === true">❤️</span></h5></div>
    <ul>
      <li>
        <div v-if="review"> 작성자 | 
      <router-link :to="{name : 'AnotherInfo', params : {id : review.user.id}}"> {{review.user.nickname}} </router-link>
    </div>
  </li>
    <li>
      Point | {{review.point}}
    </li>
    <li>
        Content | {{review.content}}
      </li>
  </ul>
  <div class="userinfo_content-section-title"><h4>댓글</h4>
    <li>
      댓글 입력 | <input type="text" @keyup.enter="createComment" v-model="writecomment">
      <button @click="createComment"> 제출하기</button>
    </li>
    <li v-for="comment in comments" :key="comment.id" :comment="comment">
      {{comment.content}}
    </li>
  </div>
      </div>
      </div>
    </div>
  </div>
  <div class="userinfo_overlay-app"></div>
</div>
</div>
</div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ReviewListItem',
  computed: {
    comments() {
      return this.$store.getters.comments
    },
    review() {
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
            this.$store.dispatch('getReviewDetail', this.$route.params.id)
        }) .catch((err) => console.log(err))
      }
    },
    createComment() {
      const review = this.review.id
      const content = this.writecomment
      const payload = {review : review, content : content}
      this.$store.dispatch('createComment', payload)
    }
  },
  data() {
    return {
      writecomment : ''
    }
  },
  created() {
    this.$store.dispatch('getReviewDetail', this.$route.params.id)
    this.$store.dispatch('getAnotherInfo', this.review.user.id)
    this.$store.dispatch('getUserInfo'),
    this.$store.dispatch('getCommentlist', this.$route.params.id)
  },
}

</script>

<style>

</style>