<template>
  <div class="info-text-left userinfo_all">
    <!-- <h1>UserInfo</h1>
    <p>{{ user.username }}</p>
    <p>{{ user.nickname }}</p>
    <p>{{ user.email }}</p>
    <hr>
    <p>{{user.followers}}</p>
    <p>{{user.followings}}</p>
    <p>{{}}</p>
  </div> -->
    <div class="userinfo_profile-all">
    <div class="userinfo_apple">
    <div class="userinfo_header">
      <div class="userinfo_menu-circle"></div>
      <div class="userinfo_header-profile">
      <div>{{user.username}}</div>
      </div>
    </div>
    <!-- 바디 -->
    <div class="userinfo_wrapper">
      <div class="userinfo_main-container">
      <div class="userinfo_main-header">
        <p class="userinfo_menu-link-main">{{user.nickname}}</p>
      </div>
      <div class="userinfo_content-wrapper">
        <div class="userinfo_content-section">
          <div>
            <userFollowers
            class="followers"
            :user="user" />
          </div>
          <div>
            <userFollowings
            class="followings"
            :user="user" />
          </div>
          <div class="wishmovie">
            <wishMovie :user="user" />
          </div>
          <div class="likemovie">
            <likeMovie :user="user" />
          </div>
          <div class="iswatched">
            <isWatched :user="user" />
          </div>
          <div class="likereview">
            <likeReview :user="user" />
          </div>
          <div class="myarticle">
            <myArticle :user="user" />
          </div>
        </div>
      </div>
      </div>
    </div>
  </div>
  <div class="userinfo_overlay-app"></div>
</div>
</div>


</template>

<script>
import userFollowers from '@/components/user/userFollowers.vue'
import userFollowings from '@/components/user/userFollowings.vue'
import myArticle from '@/components/user/myArticle'
import likeReview from '@/components/user/likeReview'
import likeMovie from '@/components/user/likeMovie'
import wishMovie from '@/components/user/wishMovie'
import isWatched from '@/components/user/isWatched'

export default {
  name: 'UserInfoView',
  components: {
    userFollowers,
    userFollowings,
    myArticle,
    likeReview,
    likeMovie,
    isWatched,
    wishMovie,
  },
  computed: {
    user() {
      return this.$store.getters.user
    }
  },
  data() {
    return {
      tf1 : false,
      tf2 : false,
      tf3 : false,
      tf4 : false,
      tf5 : false,
      tf6 : false,
      tf7 : true,
    }
  },
  methods : {
    clickfollowers() {
      document.querySelector('.followers').classList.add('is-active')
      document.querySelector('.followings').classList.remove('is-active')
      document.querySelector('.followings').classList.add('no-active')
      document.querySelector('.wishmovie').classList.remove('is-active')
      document.querySelector('.wishmovie').classList.add('no-active')
      document.querySelector('.likemovie').classList.remove('is-active')
      document.querySelector('.likemovie').classList.add('no-active')
      document.querySelector('.iswatched').classList.remove('is-active')
      document.querySelector('.iswatched').classList.add('no-active')
      document.querySelector('.likereview').classList.remove('is-active')
      document.querySelector('.likereview').classList.add('no-active')
      document.querySelector('.myarticle').classList.remove('is-active')
      document.querySelector('.myarticle').classList.add('no-active')
    
    },
    clickfollowings() {
      this.tf1 = false
      this.tf2 = true
      this.tf3 = false
      this.tf4 = false
      this.tf5 = false
      this.tf6 = false
      this.tf7 = false
    },
    clickwishmovie() {
      this.tf1 = false
      this.tf2 = false
      this.tf3 = true
      this.tf4 = false
      this.tf5 = false
      this.tf6 = false
      this.tf7 = false
    },
    clicklikemovie() {
      this.tf1 = false
      this.tf2 = false
      this.tf3 = false
      this.tf4 = true
      this.tf5 = false
      this.tf6 = false
      this.tf7 = false
    },
    clickwatched() {
      this.tf1 = false
      this.tf2 = false
      this.tf3 = false
      this.tf4 = false
      this.tf5 = true
      this.tf6 = false
      this.tf7 = false
    },
    clicklikereview() {
      this.tf1 = false
      this.tf2 = false
      this.tf3 = false
      this.tf4 = false
      this.tf5 = false
      this.tf6 = true
      this.tf7 = false
    },
    clickmyarticle() {
      this.tf1 = false
      this.tf2 = false
      this.tf3 = false
      this.tf4 = false
      this.tf5 = false
      this.tf6 = false
      this.tf7 = true
    }
  },
  created() {
    this.$store.dispatch('getUserInfo')
  }
}
</script>

<style>
.is-active {
  display : flex;
}
.no-active {
  display : none;
}

</style>