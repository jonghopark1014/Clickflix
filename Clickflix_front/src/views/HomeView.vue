<template>
  <div class="home">
    <div style="position:relative; width: 100%;" >
      <img style="max-width:100%; max-height:100%; width:auto; height:auto;" class="d-block w-100" :src='`https://image.tmdb.org/t/p/original${mainimg.backdrop_path}`' alt="">
      <div class="video">
        <div class="video-ratio">
          <iframe :src="`https://www.youtube.com/embed/${mainimg.youtube_key}?autoplay=1&mute=1`"></iframe>
        </div>
      </div>
      <div class="comment-out">
        <div class="comment-inner">
          <div>{{ mainimg.title }}</div>
          <div>{{ mainimg.runtime }} min</div>
          <br>
          <p type="button" class="btn btn-outline-danger" @click="modalbtnclick(mainimg)">Detail</p>
        </div>
      </div>
    </div>
    <h1>Your Recommend</h1>
    <swiper class="swiper" :options="swiperOption" >
      <swiper-slide v-for="movie in recommend1" :key=movie.id >
        <div class="box-wrap sizefix" >
          <div class="box btnmain">
            <div class="img" @click="MainImg(movie)" >
              <img :src='`https://image.tmdb.org/t/p/original${movie.poster_path}`' alt="Hover Effect">
            </div>
            <div class="info" @click="MainImg(movie)">
              <h3>{{ movie.title }}</h3>
              <p>{{ movie.release_date }}</p>
              <p type="button" class="btn btn-outline-danger" style="font-size:5px" @click="modalbtnclick(movie)">Detail</p>
            </div>
          </div>
        </div>
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>

    <h3>How about this Movies</h3>
    <swiper class="swiper" :options="swiperOption" >
      <swiper-slide v-for="movie in recommend2" :key=movie.id>
        <div class="box-wrap sizefix">
          <div class="box btnmain">
            <div class="img">
              <img :src='`https://image.tmdb.org/t/p/original${movie.poster_path}`' alt="Hover Effect">
            </div>
            <div class="info">
              <h3>{{ movie.title }}</h3>
              <p>{{ movie.release_date }}</p>
            </div>
          </div>
        </div>
      </swiper-slide>
      <div class="swiper-button-prev" slot="button-prev"></div>
      <div class="swiper-button-next" slot="button-next"></div>
    </swiper>

    <!-- 모달 -->
    <div style="width:100%">
      <div v-if="modal">
        <div class="modalbody modal" @click="modelclick">
          <div class="window macos modal_body">
            <div class="header">
              <div class="buttons">
                <div class="btn close"><i class="material-icons">close</i></div>
                <div class="btn minus"><i class="material-icons">remove</i></div>
                <div class="btn expand"><i class="material-icons">swap_horiz</i></div>
              </div>
              <div class="title">
                <div class="icon"><i class="material-icons">movie</i></div>
                <div class="text">CLICKFLIX</div>
              </div>
            </div>
            <img style="width: 100%;" :src='`https://image.tmdb.org/t/p/original${modal.backdrop_path}`' alt="Hover Effect">
            <div class="form container">
              <div class="row">
                <div class="col">
                  <p>영화 제목 : {{ modal.title }}</p>
                  <p>영화 장르 : </p><p v-for="genre in modal.genres" :key="genre">{{genre.name}}</p>
                  <p>배우 : </p><p v-for="actor in modal.actors" :key="actor">{{actor.name}}</p>
                  <p>개봉일 : {{modal.release_date}}</p>
                  <p>유명도 : {{modal.popularity}}</p>
                  <p>투표수 : {{modal.vote_count}}</p>
                  <p>평점 : {{modal.vote_average}}</p>
                </div>
                <div class="col">
                  <p>내용 : {{modal.overview}}</p>
                  <p>성인 : {{modal.adult}}</p>
                  <p>런타임 : {{modal.runtime}}</p>
                  <p>영화 리뷰 : {{modal.review_set}}</p>
                  <p>명대사 : {{modal.famousline_set}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import { Swiper, SwiperSlide } from "vue-awesome-swiper";
import "swiper/css/swiper.css";

export default {
  name: 'HomeView',
  components: {
    Swiper,
    SwiperSlide
  },
  data() {
    return {
      searchMovie: '',
      // mainimg: this.$store.getters.mainimg,
      // 케러셀
      swiperOption: {
        slidesPerView: 5,
        spaceBetween: 20,
        // slidesPerGroup: 5,
        loop: true,
        loopFillGroupWithBlank: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
        }
      },
    }
  },
  methods: {
    MainImg(movie) {
      this.$store.state.mainImg = movie
    },
    entersearch(event) {
      this.searchMovie = event.target.value
      console.log(this.searchMovie)
    },
    modalbtnclick(event) {
      const body = document.querySelector('.home');
      // console.log(body)
      const modal = document.querySelector('.modal');
      // console.log(modal)
      this.$store.dispatch('getModalDetail', event.id)
      if (modal.classList.contains('show')) {
        modal.classList.toggle('hidden');

      } else {
        modal.classList.toggle('show');
        if (!modal.classList.contains('show')) {
            body.style.overflow = 'auto';
          }
      }
    },
    modelclick (event) {
      const body = document.querySelector('.home');
      // console.log(body)
      const modal = document.querySelector('.modal');
      // console.log(modal)
      if (event.target === modal) {
        modal.classList.toggle('show');

        if (!modal.classList.contains('show')) {
          body.style.overflow = 'auto';
        }
      }
    }
  },
  computed: {
    // 1 는 잘보는거 추천
    recommend1() {
      return this.$store.state.recommend.slice(0, 15)
    },
    // 잘안보는거중 추천
    recommend2() {
      return this.$store.state.recommend.slice(15, 25)
    },
    mainimg() {
      return this.$store.getters.mainimg
    },
    modal() {
      return this.$store.getters.modal
    }
  },
  created() {
    this.$store.dispatch('getRecommend')
    this.$store.dispatch('getallmovie')
  },

}
</script>

<style>
.video{
  position:absolute;
  top: 5%;
  right: 3%;
  width: 55%;
  animation: fadein 5s;
  /* opacity: 0;
  transition: 1s; */
}

@keyframes fadein {
  0% {
    opacity: 0;
  }
  10% {
    opacity: 0.1;
  }
  20% {
    opacity: 0.2;
  }
  30% {
    opacity: 0.3;
  }
  40% {
    opacity: 0.4;
  }
  50% {
    opacity: 0.5;
  }
  60% {
    opacity: 0.6;
  }
  70% {
    opacity: 0.7;
  }
  80% {
    opacity: 0.8;
  }
  90% {
    opacity: 0.9;
  }
  100% {
    opacity: 1;;
  }
}

.video:hover {
  opacity: 0.4;
}

.video-ratio{
  height: 100%;
  width: 100%;
  padding-top: 56.25%;
  /* position: relative; */
}
iframe{
  background: black;
  position: absolute;
  border-radius:10px;
  top:0;
  left: 0;
  width: 100%;
  height: 100%;
}

.comment-out {
  background-color: rgb(0, 0, 0, 0.6);
  position: absolute;
  border-radius:10px;
  bottom: 5%;
  left: 2%;
  width: auto;
  height: auto;
  color: #ffffff;
}
.comment-inner {
  padding : 4px;
  height: 100%;
  width: 100%;
}

</style>