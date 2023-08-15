<template>
  <div class="userinfo_all">
    <div class="userinfo_content-section">
    <div class="userinfo_content-section-title">Followings</div>
        <ul>
          <li class="userinfo_adobe-product" v-for="following in user.followings" :key="following.id">
          <div class="userinfo_products">
            {{following.nickname}}
          </div>
          <div class="userinfo_button-wrapper">
            <button class="userinfo_content-button userinfo_status-button userinfo_open" @click="click">Open</button>
          </div>
          </li>
        </ul>
      </div>
      </div>
</template>

<script>
export default {
  name: 'userFollowings',
  props: {
    user : Object,
  },
  methods : {
    click() {
      console.log(this.user.review_user[0].movie)
    }
  }
}
</script>

<style>

</style>