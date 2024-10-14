<template>
  <div class="recommendMovie-container">
    <div class="recommend-title-container">
      <div class="title-area" @click="scrollToTop">
        <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="30" height="30" fill="url(#pattern0_186_4)"/>
        <defs>
        <pattern id="pattern0_186_4" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_186_4" transform="scale(0.0333333)"/>
        </pattern>
        <image id="image0_186_4" width="30" height="30" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAsTAAALEwEAmpwYAAABgklEQVR4nO2WPUsDQRCGD2NsNJUasDdNtPAfiH0KTTCW2qWIH+jPCFb6E9T4UwSx8QMSjUmt2EULrR6ZOMKyRG9v7xIE88JBCPPOczs7u3NBMNJfETABlIE60ATe9HkAzoANIJ00tAi0CdcjsJYEcAyoGYmvgV0gD0zqs6D/3Rlxh3HBNU30DlTkRUJesqqxovk45UUTLUfwLQGbcRqp3cNCxSvJV55j4CiKoWzs6Y/ldayYqOhqOlfDjid0BngywC9A1sV4r4a8J1jOuq26i7GrwRlPsFwwthq/GeQWstX0hGfU/zq4EvURsKj+lkvwtFdT9M91oDlOXA0lA1zyhKaMK3R9cAffErCt0A4wHvgI2JJrMEL8CvCh4IIvNGfc19WQIZHSlX5Dn4FZL7BIRpyx57Jve9qxMhKn9Pe+NRYFKrr1bc6egFUd8mGSPS3IShWaCDytw+PU+vRpyZGR7jUbSWCJwaNKV36j8AYwF/wXeNYo++XQwAb8CrgYKnikQPUJRJkZfOuuONUAAAAASUVORK5CYII="/>
        </defs>
        </svg>
        <p>다른 조건 검색</p>
      </div>
    </div>
    <div class="wrapper">
      <div class="username-title">
        <p><strong>{{ store.user }}</strong>님에게 꼭 맞는 <strong>ShihTzu</strong></p>
      </div>
      <div class="carousel-container">
        <Carousel 
          :autoplay="isAutoplay" 
          :wrap-around="true" 
          :transition="500" 
          v-model="currentSlideIndex"
          :pauseAutoplayOnHover="true"
        >
          <slide v-for="slide in movies" :key="slide" class="hi">
            <div class="slide-inner">
              <div class="slide-title">
                <p class="wrapper_title"><strong>|</strong> {{ slide.title }}</p>
                <p class="wrapper_date"><strong>개봉일 </strong> {{ slide.released_date}}</p>
              </div>
              <div class="carousel__item" @click="openModal(slide)">
                <img :src="`https://image.tmdb.org/t/p/original${slide.backdrop_path}`" width="90%" height="auto" class="slideImg1" alt="포스터가 없는 영화입니다.">
              </div>
            </div>
          </slide>
      
          <template #addons>
            <navigation />
            <pagination />
          </template>
        </Carousel>
      </div>
    </div>
    <MovieModal 
      :isModalOpen="isModalOpen" 
      :currentSlide="currentSlide"
      @closeModal="closeModal"
      @movieSelected="openModal"
    />
  </div>
</template>

<script setup>
import { defineComponent, ref, watch, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import MovieModal from '@/components/MovieModal.vue';
import "vue3-carousel/dist/carousel.css";

const store = useAuthStore()

const isModalOpen = ref(false);
const currentSlide = ref({});
const isAutoplay = ref(3000);
const currentSlideIndex = ref(0); // 현재 슬라이드 인덱스

const openModal = (slide) => {
  currentSlide.value = slide;
  isModalOpen.value = true;
  isAutoplay.value = 0; // Stop the autoplay
};

const closeModal = () => {
  isModalOpen.value = false;
  isAutoplay.value = 3000; // Resume the autoplay
};


const props = defineProps({
  movies: Array,
});

defineComponent({
  name: 'Autoplay',
  components: {
    Carousel,
    Slide,
    Pagination,
    Navigation,
  },
});

const resetCarousel = () => {
  currentSlideIndex.value = 0;
  isAutoplay.value = 3000;
};


const scrollToTop = () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
};


// movies가 변경될 때 첫 번째 슬라이드로 이동
watch(() => props.movies, () => {
  currentSlideIndex.value = 0;
});


</script>

<style scoped>
.recommend-title-container{
  display: flex;
  justify-content: center;
}
.slide-title {
  display: flex;
  justify-content: space-between;
  flex-direction: row;
  align-items: center;
  color: rgb(165, 165, 165);
  align-self: flex-start;
  margin-bottom: 10px;
  font-size: 20px;
  width: 100%;
}
.tiny-title {
  align-self: flex-end;
  margin-left: 20px;
}
.recommendMovie-container{
  width: 100%;
  height: 92vh;
}
.title-area{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  width: 10%;
  height: 12vh;
  cursor: pointer;
  transition: transform 0.3s ease-in-out;
}
.title-area:hover {
  transform: scale(1.15);
}
.title-area > p {
  margin-top: 10px;
  color: #eeeeee;
}
.RecommendMovieTitle {
  font-size: 17px;
  color: black;
  
}
.wrapper {
  height: 80vh;
  display: flex;
  flex-direction: column;
  justify-content: center;

  align-items: center;
  background-color: #1b1b1b;
  border-top-right-radius: 40px;
  border-top-left-radius: 40px;
}
.wrapper_title{
  color: #eeeeee;
  align-self: flex-start;
  margin-left: 6%;
  font-size: 20px;
}
.wrapper_date {
  margin-right: 5%;
}
.slide-inner {
  display: flex;
  flex-direction: column;
  width: 100%;
}
.carousel-container {
  width: 95%;
}
.carousel__item {
  height: 60vh;
	font-size: 20px;
	border-radius: 8px;
  cursor: pointer;
	/* display: flex;
  flex-direction: row;
	justify-content: center;
	align-items: center; */
}
.carousel__prev,
.carousel__next {
  color: rgb(165, 165, 165);
}
.slideImg1 {
  margin-left: 20px;
  color: white;
  font-size: 30px;
  
}
.hi {
  margin-top: 40px;
}
.username-title {
  width: 100%;
  color: #eeeeee;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.username-title > p {
  margin-left: 50px;
  font-size: 20px;
}
</style>
