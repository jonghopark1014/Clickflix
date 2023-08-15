<template>
  <div class="info-text-left userinfo_all">
    <div class="userinfo_profile-all">
    <div class="userinfo_apple">
    <div class="userinfo_header">
      <div class="userinfo_menu-circle"></div>
      <div class="userinfo_header-profile">
      <div>   </div>
      </div>
    </div>
    <!-- 바디 -->
    <div class="userinfo_wrapper">
      <div class="userinfo_main-container">
      <div class="userinfo_main-header">
        <p class="userinfo_menu-link-main">{{ movie?.title }}</p>
        
      </div>
      <div class="userinfo_content-wrapper">
        <div class="userinfo_content-section">
          <div>
            <img style="max-width:100%; max-height:100%; width:auto; height:auto;" class="d-block w-100" :src='`https://image.tmdb.org/t/p/original${movie?.backdrop_path}`' alt="">
          </div>
          <div class="form container">
              <div class="row">
                <div class="col">
                  <p>영화 제목 : {{ movie?.title }}</p>
                  <p>영화 장르 : </p><p v-for="genre in movie?.genres" :key="genre">{{genre.name}}</p>
                  <p>배우 : </p><p v-for="actor in movie?.actors" :key="actor">{{actor.name}}</p>
                  <p>개봉일 : {{movie?.release_date}}</p>
                  <p>유명도 : {{movie?.popularity}}</p>
                  <p>투표수 : {{movie?.vote_count}}</p>
                  <p>평점 : {{movie?.vote_average}}</p>
                </div>
                <div class="col">
                  <p>내용 : {{movie?.overview}}</p>
                  <p>성인 : {{movie?.adult}}</p>
                  <p>런타임 : {{movie?.runtime}}</p>
                  <p>영화 리뷰 : {{movie?.review_set}}</p>
                  <p>명대사 : {{movie?.famousline_set}}</p>
                </div>
              </div>
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

<!-- <template>
  <div>
    <h1>Detail</h1>
    <p>영화 제목 : {{ movie?.title }}</p>
    <p>영화 장르 : {{movie.genres}}</p>
    <p>배우 : {{movie.actors}}</p>
    <p>개봉일 : {{movie.release_date}}</p>
    <p>유명도 : {{movie.popularity}}</p>
    <p>투표수 : {{movie.vote_count}}</p>
    <p>OTT : {{movie.providers}}</p>
    <p>평점 : {{movie.vote_average}}</p>
    <p>내용 : {{movie.overview}}</p>
    <p>성인 : {{movie.adult}}</p>
    <p>런타임 : {{movie.runtime}}</p>
    <p>영화 리뷰 : {{movie.review_set}}</p>
    <p>명대사 : {{movie.famousline_set}}</p>
    <p>{{movie}}</p>
    <p>영화 좋아요 수{{islikecount}}</p>
    <p @click="getLike" v-if="islike === false">영화 좋아요 ♡</p>
    <p @click="getLike" v-if="islike === true">영화 좋아요 ❤️</p>
    <p @click="wishwatch" v-if="iswishwatch === false">워치리스트에 넣기 : +</p>
    <p @click="wishwatch" v-if="iswishwatch === true">워치리스트에서 빼기 : +</p>
    <p @click="watched" v-if="iswatched === false">본영화 체크 : +</p>
    <p @click="watched" v-if="iswatched === true">본영화 체크빼기 : +</p>
  </div>
</template> -->

<script>
import axios from 'axios'

export default {
  name: 'MovieDetailView',
  computed: {
    movie() {
      return this.$store.getters.movie
    },
    user() {
      return this.$store.getters.user
    },
    islike() {
      const value = this.movie.like_users.includes(this.user.id) ? true : false;
      return value
    },
    islikecount() {
      return this.movie.like_users.length
    },
    iswishwatch() {
      const value = this.movie.wish_watch.includes(this.user.id) ? true : false
      return value
    },
    iswatched() {
      const value = this.movie.is_watched.includes(this.user.id) ? true : false
      return value
    }
  },
  methods: {
    getLike() {
      const movie_id = this.movie.id
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user) {
        axios({
          url : `${API_URL}/api/v1/movies/${movie_id}/like/`,
          method : 'post',
          headers : this.$store.getters.authHead,
        })
          .then((res) => {
          console.log(res.data.like_count)
        }) .catch((err) => console.log(err))
      }
      this.$store.dispatch('getMovieDetail', movie_id)
    },
    wishwatch() {
      const movie_id = this.movie.id
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user) {
        axios({
          url: `${API_URL}/api/v1/movies/${movie_id}/wish/`,
          method : 'post',
          headers : this.$store.getters.authHead,
        })
          .then(() => {
            this.$store.dispatch('getMovieDetail', movie_id)
          })
          .catch((err) => console.log(err))
      }
    },
    watched() {
      const movie_id = this.movie.id
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user) {
        axios({
          url: `${API_URL}/api/v1/movies/${movie_id}/watched/`,
          method : 'post',
          headers : this.$store.getters.authHead,
        })
          .then(() => {
            this.$store.dispatch('getMovieDetail', movie_id)
          })
          .catch((err) => console.log(err))
      }
    }
  },
  created() {
    this.$store.dispatch('getMovieDetail', this.$route.params.id)
    this.$store.dispatch('getUserInfo')
  },
}
</script>

<style>

</style>