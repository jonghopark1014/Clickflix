import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)
const API_URL = 'http://127.0.0.1:8000'

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    // user
    token : null,
    user : null,
    another : null,
    // movie
    mainImg: null,
    cnt : 0,
    recommend: [],
    listall: [],
    movie: {},
    random: null,
    modal : null,
    // // movie like
    islike : {},
    islikecount : {},
    // search
    searchmovie: '',
    searchlist: null,
    searchword: '',
    // review
    reviews: {},
    review: {},
    // // reivew like
    islikereview : null,
    islikereviewcount : null,
    // Comments
    comments: {},
    // // Comments like
    islikecomment : null,
    islikecommentcount : null,
    // famousline
    famousline: {},
    famouslines : {},
    // 더미 데이터 (리뷰리스트, 커뮤니티, 명언, 유저정보)

    userInfo: {
      username: 'qkrqkrgh',
      nickname: 'qkrqkrghfkddl',
      email: 'qkrqkrgh@gamil.com',
    }
  },
  getters: {
    // movie
    recommend: (state) => state.recommend,
    modal: (state) => state.modal,
    movie: (state) => state.movie,
    listall: (state) => state.listall,
    random: (state) => state.random,
    mainimg: (state) => state.mainImg,
    // search
    searchmovie: (state) => state.searchmovie,
    // review
    review: (state) => state.review,
    // comments
    comments: (state) => state.comments,
    // famousline
    famousline: (state) => state.famousline,
    famouslines: (state) => state.famouslines,
    // user
    isLogin: (state) => state.token ? true : false,
    authHead: (state) => ({ Authorization: `Token ${state.token}`}),
    user: (state) => state.user,
    another: (state) => state.another,
  },
  mutations: {
    // movies
    SET_RECOMMEND: (state, recommend) => {state.recommend = recommend, state.mainImg = recommend[0]},
    SET_LISTALL: (state, listall) => {state.listall = listall, state.cnt += 1},
    SET_MOVIE: (state, movie) => state.movie = movie,
    SET_MODAL: (state, movie) => state.modal = movie,
    SET_ALLRANDOM: (state, random) => state.random = random,
    // search
    SET_SEARCH: (state, keyword) => {
      // console.log(keyword)
      state.searchword = keyword
      let searchli = []
      if (keyword === '') {
        state.searchlist = []
      } else {

        let tmp_num = 0
        while (tmp_num < 51) {

        
        if (tmp_num > 50) {
          break;
        } 
        let a = Math.round(Math.random() * state.listall.length)
        let movie = state.listall[a]
          if (movie.title.split(' ').join('').includes(keyword.split(' ').join('')) && !searchli.includes(movie)) {
            searchli.push(movie)
            tmp_num += 1;
          }
          for (const genre of movie.genres) {
            if (genre.name.split(' ').join('').includes(keyword.split(' ').join('')) && !searchli.includes(movie)) {
              searchli.push(movie)
              tmp_num += 1;
            }
          }
          for (const actor of movie.actors) {
            if (actor.name.split(' ').join('').includes(keyword.split(' ').join('')) && !searchli.includes(movie)) {
              searchli.push(movie)
              tmp_num += 1;
            }
            for (const character of actor.actorcharacter_set) {
              if (character.character.split(' ').join('').includes(keyword.split(' ').join('')) && !searchli.includes(movie)) {
                searchli.push(movie)
                tmp_num += 1;
              }
            }
            for (const known of actor.actorasknown_set)
            if (known.asknown.split(' ').join('').includes(keyword.split(' ').join('')) && !searchli.includes(movie)) {
              searchli.push(movie)
              tmp_num += 1;
            }
          }
        // console.log(searchli)
        state.searchlist = searchli
      }
    }
    },
    // review
    SET_REVIEWS: (state, reviews) => state.reviews = reviews,
    SET_REVIEW:(state, review) => state.review = review,
    SEARCHMOVIE: (state, movie) => state.searchmovie = movie,
    // // review like
    GET_LIKE_REVIEW: (state, data) => {state.islikereview = data.is_liked, state.islikereviewcount = data.like_count},
    SET_LIKE_REVIEW: (state, user) => {
      if (state.review.like_users.includes(user)) {
        state.islike = true
      } else {
        state.islike = false
      }
    },

    // Comment
    SET_COMMENT: (state, comments) => state.comments = comments,
    // // Comment like
    GET_LIKE_COMMENT: (state, data) => {state.islikecomment = data.is_liked, state.islikecommentcount = data.like_count},
    SET_LIKE_COMMENT: (state, user) => {
      if (state.comments.like_users.includes(user)) {
        state.islike = true
      } else {
        state.islike = false
      }
    },

    // famousline
    SET_FAMOUSLINES: (state, famouslines) => state.famouslines = famouslines,
    SET_FAMOUSLINE: (state, famousline) => state.famousline = famousline,
    // user
    SAVE_TOKEN : (state, token) => state.token = token,
    SET_TOKEN : (state) => state.token = null,
    SET_USER: (state,user) => state.user = user,
    SET_ANOTHER: (state, user) => state.another = user,
  },
  actions: {
    // movies
    getRecommend( {commit, state, getters} ) {
      if (!state.user) {
        axios({
          url: `${API_URL}/api/v1/movies/recommend/anonymous/`,
          method: 'get',
        })
        .then((res) => {
          console.log(res)
          commit('SET_RECOMMEND', res.data)
        })
        .catch((err) => console.log(err))
      }
      else {
        const user = state.user
        console.log(user.id)
        axios({
          url: `${API_URL}/api/v1/movies/recommend/${user.id}/`,
          method: 'post',
          headers: getters.authHead,
        })
        .then((res) => {
          console.log(res)
          commit('SET_RECOMMEND', res.data)
        })
        .catch((err) => console.log(err))
      }
    },
    getallmovie( {commit, state} ) {
      if (state.cnt === 0) {
      axios({
        url: `${API_URL}/api/v1/movies/listall/`,
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        commit('SET_LISTALL', res.data)
      })
      .catch((err) => console.log(err))
    }},
    getMovieDetail( {commit}, movieid ) {
      axios({
        url: `${API_URL}/api/v1/movies/${movieid}`,
      })
      .then((res) => {
        console.log(res)
        commit('SET_MOVIE', res.data)
      })
      .catch((err) => console.log(err))
    },
    getModalDetail( {commit}, movieid ) {
      axios({
        url: `${API_URL}/api/v1/movies/${movieid}`,
      })
      .then((res) => {
        console.log(res)
        commit('SET_MODAL', res.data)
      })
      .catch((err) => console.log(err))
    },
    getAllrandom( {commit} ) {
      axios({
        url: `${API_URL}/api/v1/movies/recommend/allrandom/`,
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        commit('SET_ALLRANDOM', res.data)
      })
      .catch((err) => console.log(err))
    },
    // search
    searching( {commit}, searchword) {
      // console.log(searchword)
      commit('SET_SEARCH', searchword)
    },
    // reviews
    getReviews( {commit} ) {
      axios({
        url: `${API_URL}/api/v1/community/review/list/`,
        method: 'get',
      })
      .then((res) => {
        console.log(res)
        commit('SET_REVIEWS', res.data)
      })
      .catch((err) => console.log(err))
    },
    getReviewDetail( {commit}, reviewid ) {
      console.log(222222222222222)
      axios({
        url: `${API_URL}/api/v1/community/review/${reviewid}/`
      })
      .then((res) => {
        console.log(res.data)
        commit('SET_REVIEW', res.data)
      })
      .catch((err) => console.log(err))
    },
    createReview( {getters}, payload ) {
      const movieid = payload.movieid
      const title = payload.title
      const point = payload.point
      const content = payload.content
      const result = { title: title, point: point, content: content }
      // console.log(result)
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/community/review/${movieid}/create/`,
        headers: getters.authHead,
        data: {...result}
      })
      .then(() => {
        router.push({ name: 'Community' })
      })
      .catch((err) => console.log(err))
    },
    UpdateReview( {getters}, payload ) {
      const reviewid = payload.reviewid
      const movieid = payload.movieid
      const title = payload.title
      const point = payload.point
      const content = payload.content
      const result = {movie : movieid, title: title, point: point, content: content,}
      // console.log(result)
      axios({
        method: 'put',
        url: `${API_URL}/api/v1/community/review/edit/${reviewid}/`,
        headers: getters.authHead,
        data: {...result}
      })
      .then(() => {
        router.push({ name: 'ReviewView' })
      })
      .catch((err) => console.log(err))
    },
    reviewpick( {commit}, movie ) {
      commit('SEARCHMOVIE', movie)
    },
    reviewdelete( {getters}, reviewid ) {
      console.log(reviewid);
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/review/edit/${reviewid}/`,
        headers: getters.authHead,
      })
      .then(() => {
        router.push({ name: 'ReviewView' })
      })
      .catch((err) => console.log(err))
    },
    // // review like
    getLikeReview({commit, getters}, reviewid) {
      const review_id = reviewid
      if (this.state.user) {
        axios({
          url: `${API_URL}/api/v1/community/review/${review_id}/like/`,
          method:'post',
          headers : getters.authHead,
        })
          .then((res) => {
            commit('GET_LIKE_REVIEW', res.data)
          })
      }
    },
    setLikeReview({commit}, payload) {
      commit('SET_LIKE_REVIEW', payload)
    },
    // comment
    createComment({getters}, payload) {
      const review = payload.review
      const content = payload.content
      const result = {review : review, content : content}
      axios({
        method: 'post',
        url:  `${API_URL}/api/v1/community/review/${review}/comment/`,
        headers : getters.authHead,
        data: {...result}
      })
        .then(() => {
          router.go(router.currentRoute)
        })
    },
    getCommentlist({commit}, reviewid) {
      const reviewidd = reviewid
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/community/${reviewidd}/comment/`
      })
      .then((res) => {
        commit('SET_COMMENT', res.data)
      })
      .catch((res) => {
        commit('SET_COMMENT', res.data)
      })
    },
    commentDelete({getters}, payload) {
      const commentpk = payload
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/comment/${commentpk}/edit/`,
        headers: getters.authHead,
      })
      .then(() => {
        router.go(router.currentRoute)
      })
      .catch((err) => console.log(err))
    },
    commentUpdate({getters}, payload) {
      const review = payload.review
      const content = payload.content
      const commentpk = payload.commentpk
      const result = {review : review, content : content}
      axios({
        method:'put',
        url: `${API_URL}/api/v1/community/comment/${commentpk}/edit/`,
        headers : getters.authHead,
        data: {...result}
      })
        .then(() => {
          router.go(router.currentRoute)
        })
    },
    // // comment like
    getLikeComment({commit, getters}, commentid) {
      const comment_id = commentid
      if (this.state.user) {
        axios({
          url : `${API_URL}/api/v1/community/comment/${comment_id}/like/`,
          method: 'post',
          headers: getters.authHead,
        })
          .then((res) => {
            commit('GET_LIKE_COMMENT', res.data)
          })
      }
    },
    setLikeComment({commit}, payload) {
      commit('SET_LIKE_COMMENT', payload)
    },
    // famous line
    famouslineDelete( {getters, dispatch}, famouslineid ) {
      const famousLineid = famouslineid
      console.log(famousLineid);
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/community/famousline/${famousLineid}/edit/`,
        headers: getters.authHead,
      })
      .then(() => {
        dispatch('getFamouslines')
      })
      .catch((err) => console.log(err))
    },
    getFamousline({commit}, famouslineidd) {
      const famouslineid = famouslineidd
      axios({
        url : `${API_URL}/api/v1/community/famousline/${famouslineid}/`,
        method : 'post',
        headers: this.getters.authHead,
      })
      .then((res) => {
        commit('SET_FAMOUSLINE', res.data)
      })
      .catch((err) => console.log(err))
    },
    getFamouslines({commit}) {
      axios({
        url: `${API_URL}/api/v1/community/famousline/list/`,
        method : 'get',
      })
      .then((res) => {
        commit('SET_FAMOUSLINES', res.data)
      })
      .catch((err) => console.log(err))
    },
    createFamousline({getters}, payload) {
      const movieid = payload.movieid
      const content = payload.content
      const speaker = payload.speaker
      const result = { content : content, speaker : speaker}
      axios({
        method: 'post',
        url : `${API_URL}/api/v1/community/famousline/${movieid}/create/`,
        headers: getters.authHead,
        data: {...result}
      })
        .then(() => {
          router.push({name: 'FamousLine'})
        })
        .catch((err) => console.log(err))
    },
    updateFamousline({getters}, payload) {
      const famouslineid = payload.famouslineid
      const movieid = payload.movieid
      const content = payload.content
      const speaker = payload.speaker
      const result = {movie : movieid, content : content, speaker : speaker}
      axios({
        method : 'put',
        url : `${API_URL}/api/v1/community/famousline/${famouslineid}/edit/`,
        headers : getters.authHead,
        data : {...result}
      })
        .then(() => {
          router.push({name : 'FamousLine'})
        })
        .catch((err) => console.log(err))
    },
    // user
    signUp( {commit, dispatch}, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {...payload}
      })
      .then((res) => {
        commit('SAVE_TOKEN', res.data.key)
        dispatch('getUserInfo')
        router.push({name: 'home'})
      })
      .catch((err) => alert(JSON.stringify(err.response.data)))
    },
    login( {commit, dispatch }, { username, password, email }) {
      const payload = { username, password, email }
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: payload
      })
      .then((res) => {
        commit('SAVE_TOKEN', res.data.key)
        dispatch('getUserInfo')
        router.push({ name: 'home' })
        router.go()
      })
      .catch((err) => alert(JSON.stringify(err.response.data )))
    },
    logout({commit, getters}) {
      axios({
        url: `${API_URL}/accounts/logout/`,
        method: 'post',
        headers: getters.authHead,
      })
      .then((res) => {
        console.log(res)
        commit('SET_TOKEN')
        commit('SET_USER', null)
        localStorage.removeItem('vuex')
        router.push({ name: 'home' })
      })
      .catch((err) => console.log(err))
    },
    getUserInfo({commit, getters}) {
      axios({
        url: `${API_URL}/accounts/user/`,
        method: 'get',
        headers: getters.authHead,
      })
      .then((res) => {
        console.log(res)
        commit('SET_USER',res.data)
      })
    },
    getAnotherInfo({commit}, userpk) {
      console.log(userpk)
      axios({
        url : `${API_URL}/accounts/follow/${userpk}/anotherinfo/`,
        method: 'get',
      })
        .then((res) => {
          commit('SET_ANOTHER', res.data)
        })
        .catch((err) => console.log(err))
    }
  },
  modules: {
  }
})
