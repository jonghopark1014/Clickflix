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
        </div>
      </div>
      <div class="userinfo_content-wrapper">
        <div class="userinfo_content-section">
        <div class="userinfo_content-section-title">Review Create</div>
    <ul>
      <li>
      <ReviewSearchBar />
    </li>
    <li>
      <ReviewSearchlist />
    </li>
      <li><h3>{{ searchmovie.title }}</h3></li>
    <li><form @submit.prevent="createReview">
      <label for="title">제목</label> |  
      <input type="text" id="title" v-model="title"><br>
      <label for="point">평점</label> | 
      <input type="number" id="point" v-model="point"><br>
      <label for="content">내용</label> |  
      <input type="text" id="content" v-model="content"><br>
      <input type="submit" id="submit">
    </form>
  </li>
  </ul>
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
import ReviewSearchBar from '@/components/review/ReviewSearchBar'
import ReviewSearchlist from '@/components/review/ReviewSearchlist'
export default {
  name: 'ReviewCreateView',
  components: {
    ReviewSearchBar,
    ReviewSearchlist,
  },
  data() {
    return {
      title: null,
      point: null,
      content: null,
    }
  },
  computed: {
    searchmovie() {
      return this.$store.getters.searchmovie
    },
  },
  methods: {
    createReview() {
      const payload = { movieid: this.searchmovie.id, title: this.title, point: this.point, content:this.content }
      this.$store.dispatch('createReview', payload)
      this.$store.state.searchmovie = ''
    },

  }
}
</script>

<style>

</style>