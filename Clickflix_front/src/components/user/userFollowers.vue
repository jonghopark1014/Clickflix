<template>
  <div class="userinfo_all">
    <div class="userinfo_content-section">
    <div class="userinfo_content-section-title">Followers</div>
        <ul>
          <li class="userinfo_adobe-product" v-for="follower in user.followers" :key="follower.id">
          <div class="userinfo_products">
            {{follower.nickname}}
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
  name: 'userFollowers',
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