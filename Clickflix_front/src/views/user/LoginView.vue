<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: null,
      password: null,
    }
  },
  methods: {
    logIn() {
      const username = this.username
      const password = this.password
      const email = ''

      const payload = {
        username: username,
        password: password,
        email : email,
      }
      this.$store.dispatch('login', payload)
    }
  }
}
</script>

<style>

</style>