<template>
  <div>
    <h1>UserInfo</h1>
    <p>{{ another.username }}</p>
    <p>{{ another.nickname }}</p>
    <p>{{ another.email }}</p>
    <button @click="follow" v-if="isfollow === false">follow</button>
    <button @click="follow" v-if="isfollow === true">isFollowed</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'UserInfoView',
  computed: {
    another() {
      return this.$store.getters.another
    },
    user() {
      return this.$store.getters.user
    },
    isfollow() {
      const value = this.another.followers.includes(this.user.id) ? true : false;
      return value
    }
  },
  methods: {
    follow() {
      console.log(this.another.id)
      const another_id = this.another.id
      const API_URL = 'http://127.0.0.1:8000'
      if (this.user) {
        axios({
          url : `${API_URL}/accounts/follow/${another_id}/follow/`,
          method : 'post',
          headers : this.$store.getters.authHead,
        })
          .then(() => {
          this.$store.dispatch('getAnotherInfo', another_id)
          this.$store.dispatch('getUserInfo')
        }) .catch((err) => console.log(err))
      }
    }
  },
  created() {
    this.$store.dispatch('getAnotherInfo', this.$route.params.id)
    this.$store.dispatch('getUserInfo')
  },
}
</script>

<style>

</style>