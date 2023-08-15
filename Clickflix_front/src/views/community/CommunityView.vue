<template>
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
          <router-link :to="{ name: 'ReviewCreate' }">리뷰생성</router-link>
        </div>
      </div>
      <div class="userinfo_content-wrapper">
        <ReviewList />
        <!-- <div class="userinfo_content-section">
        <div class="userinfo_content-section-title">reviewlist</div>
        <ul>
          <li class="userinfo_adobe-product">
          <div class="userinfo_products">
            Photoshop
          </div>
          <span class="userinfo_status">
            <span class="userinfo_status-circle userinfo_green"></span>
            Updated</span>
          <div class="userinfo_button-wrapper">
            <button class="userinfo_content-button userinfo_status-button userinfo_open">Open</button>
          </div>
          </li>
        </ul>
        </div> -->
      </div>
      </div>
    </div>
  </div>
  <div class="userinfo_overlay-app"></div>
</div>
</div>
</template>

<script>
import ReviewList from '@/components/review/ReviewList'
export default {
  name: 'CommunityView',
  components: {
    ReviewList
  },
  data() {
    return {
      trueorfalse1: false,
      trueorfalse2: false
    }
  },

  methods: {
    click1() {
      this.trueorfalse2 = false
      this.trueorfalse1 = true
    },
    click2() {
      this.trueorfalse1 = false
      this.trueorfalse2 = true
    }
  },
  created() {
    this.$store.dispatch('getReviews')
  }
  

}

</script>

<style>

</style>