<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="nickname">nickname : </label>
      <input type="text" id="nickname" v-model="nickname"><br>

      <label for="username">useremail : </label>
      <input type="email" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password check : </label>
      <input type="password" id="password2" v-model="password2"><br>

      <label for="birthday"> birthday : </label>
      <input type="date" id="birthday" v-model="birthday"><br>

      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return {
      email: null,
      username: null,
      password1: null,
      password2: null,
      first_name: null,
      last_name: null,
      birthday: null,
      nickname: null,
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2
      const first_name = this.first_name
      const last_name = this.last_name
      const birthday = this.birthday
      const nickname = this.nickname


      const payload = {
        username: username,
        password1: password1,
        password2: password2,
        first_name: first_name,
        last_name: last_name,
        birthday: birthday,
        nickname: nickname,
      }
      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>
