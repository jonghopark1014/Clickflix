<template>
  <div>
    <div id="bikefu">
      <div class="bike">
        <div class="bike__cloud-1"><h1>액션</h1></div>
        <div class="bike__cloud-2"><h1>코미디</h1></div>
        <div class="bike__cloud-3"><h1>애로</h1></div>
        <div class="bike__cloud-4"><h1>코미디</h1></div>
        <div class="bike__cloud-5"><h1>드라마</h1></div>
        <div class="bike__cloud-6"><h1>공포</h1></div>
        <div class="bike__bike">
          <div class="bike__wheel">
            <div class="bike__needle"></div>
            <div class="bike__needle"></div>
            <div class="bike__needle"></div>
          </div>
          <div class="bike__wheel">
            <div class="bike__needle"></div>
            <div class="bike__needle"></div>
            <div class="bike__needle"></div>
          </div>
          <div class="bike__down-tube"></div>
          <div class="bike__tubes">
            <div class="bike__chain"></div>
            <div class="bike__seat-stays"></div>
            <div class="bike__chain-stays"></div>
            <div class="bike__seat-tube"></div>
            <div class="bike__star">
              <div class="bike__pedal"></div>
            </div>
            <div class="bike__seat"></div>
          </div>
          <div class="bike__top-tube"></div>
          <div class="bike__fo"></div>
          <div class="bike__head-tube"></div>
          <div class="bike__helm"></div>
          <div class="bike__lock"></div>
        </div>
        <div class="bike__man">
          <div class="bike__arm">
            <div class="bike__forearm">
              <div class="bike__hand"></div>
            </div>
            <div class="bike__sleeve"></div>
          </div>
          <div class="bike__back-leg">
            <div class="bike__shin">
              <div class="bike__skin"></div>
              <div class="bike__ked"></div>
            </div>
          </div>
          <div class="bike__butt"></div>
          <div class="bike__front-leg">
            <div class="bike__shin">
              <div class="bike__skin"></div>
              <div class="bike__ked"></div>
            </div>
          </div>
          <div class="bike__shirt">
            <div class="bike__collar"></div>
          </div>
          <div class="bike__arm">
            <div class="bike__forearm">
              <div class="bike__hand"></div>
            </div>
            <div class="bike__sleeve"></div>
          </div>
          <div class="bike__head">
            <div class="bike__eye"></div>
            <div class="bike__eye"></div>
            <div class="bike__whisker"></div>
            <div class="bike__nose"></div>
            <div class="bike__month"></div>
            <div class="bike__whisker"></div>
            <div class="bike__cap">
              <div class="bike__peak">
                <div class="bike__peak-parts"></div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="bike_display">
      <img style="max-width:100%; max-height:100%; width:auto; height:auto;" class="d-block w-100" :src='`https://image.tmdb.org/t/p/original${random[0].backdrop_path}`' alt="">
      <h1>{{ random[0].title }}</h1>
    </div>
  </div>
</template>

<script>
export default {
  name: 'RecommendView',
  computed: {
      random() {
        return this.$store.getters.random
        },
    },
    created() {
      this.$store.dispatch('getAllrandom'),
      setTimeout(function() {
        const bikeshow = document.querySelector("#bikefu");
        const randomshow = document.querySelector(".bike_display");
        bikeshow.classList.toggle('bike_display');
        randomshow.classList.remove('bike_display');
        // randomshow.classList.add('randomshow');
      }, 4000)
    }
}
</script>

<style>

</style>