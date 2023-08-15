<template>
  <div class="col box-wrap sizefix">
    <div class="box btnmain">
      <div class="img">
        <img :src='`https://image.tmdb.org/t/p/original${movie.poster_path}`' alt="Hover Effect">
      </div>
      <div class="info">
        <h3>{{ movie.title }}</h3>
        <span v-for="genre in movie.genres" :key="genre.id">{{ genre.name }} </span><br>
        <router-link :to="{ name: 'MovieDetail', params: { id: movie.id } }">자세히</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  }
}
</script>

<style>
.sizefix {
    overflow: hidden;
    border-radius:10px;
}

.btnmain {
  transform: scale(1);
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transition: all 0.3s ease-in-out;   /* 부드러운 모션을 위해 추가*/
}

.btnmain:hover {
  transform: scale(1.2);
  -webkit-transform: scale(1.2);
  -moz-transform: scale(1.2);
  -ms-transform: scale(1.2);
  -o-transform: scale(1.2);
}

.btnmain::before {
  position: absolute;
  top: 100%;
  left: 0%;
  transition: all 0.4s;
  z-index : -1;
}
.btnmain:hover::before {
  transform: translateY(-100%);
}
.box-wrap {
  /* border-radius:10px;  */
  /* width: 100vw;
  height: 100vh; */
  display: flex;
  justify-content: center;
  align-items: center
}
.box {
  border-radius:10px; 
  position: relative;
  width: 100%;
  /* width: 400px; height: 300px; */
  /* border: 7px solid #283593; */
  box-shadow: 1px 1px 3px rgba(0,0,0,0.4);
}
.box img {
  max-width:100%;
  max-height:100%;
  width:auto;
  height: 100%;
  border-radius:10px;
}

.box .info {
  color: #fff;
  position: absolute; left: 0; bottom: 0;
  background: rgba(0,0,0,0.5);
  width: 100%;
  padding: 15px;
  box-sizing: border-box;
  opacity: 0;
  transition: opacity 0.35s ease-in-out;
}
.box:hover .info {
  opacity: 1;
}
.box .info h3 {
  font-size: 1rem;
  padding-bottom: 0.4em;
  overflow:hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}
.box .info p {
  font-size: 20px;
  text-overflow: ellipsis;
  white-space: nowrap;
  text-transform: uppercase;
}
</style>