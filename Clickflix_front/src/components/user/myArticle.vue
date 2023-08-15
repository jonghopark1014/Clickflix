<template>
  <div class="userinfo_all">
    <div class="userinfo_content-section">
    <div class="userinfo_content-section-title">My Article</div>
        <ul>
          <li class="userinfo_adobe-product" v-for="review in user.review_user" :key="review.id">
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
      <div class="userinfo_content-section">
    <div class="userinfo_content-section-title">Comment</div>
        <ul>
          <li class="userinfo_adobe-product" v-for="comment in user.comment_set" :key="comment.id">
          <div class="userinfo_products">
            {{comment.content}}
          </div>
          <span class="userinfo_status">{{comment.review_set.movie_set}}</span>
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
  name: 'myArticle',
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