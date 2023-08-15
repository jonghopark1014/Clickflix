<template>
  <div>
    <h1>User</h1>
    <router-link :to="{ name: 'Login' }">login</router-link> |
    <router-link :to="{ name: 'Signup' }">signup</router-link> |
    <router-link :to="{ name: 'UserInfo' }">userinfo</router-link> |
  </div>
</template>

<script>
export default {
  name: 'UserView',
}
</script>

<style>

</style>