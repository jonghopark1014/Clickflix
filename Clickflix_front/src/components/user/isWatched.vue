<template>
  <div class="userinfo_all">
    <div class="userinfo_content-section">
    <div class="userinfo_content-section-title">Watched</div>
        <ul>
          <li class="userinfo_adobe-product" v-for="review in user.like_review" :key="review.id">
          <div class="userinfo_products">
            {{review.title}}
          </div>
          <span class="userinfo_status">{{review.movie_set}}</span>
          <span class="userinfo_status">{{review.point}}점</span>
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
  name : 'isWatched',
  props: {
    user : Object,
  },
}
</script>

<style>

</style>