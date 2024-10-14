<template>
  <div class="boxoffice-container _cont2">
    <p class="boxoffice-title"><strong>|</strong> Box <strong>Office</strong></p>
    <div class="carousel-container2">
      <Carousel :autoplay="isAutoplay" :itemsToShow="5" :wrapAround="true" :transition="1000" :pauseAutoplayOnHover="true">
        <Slide v-for="slide in slides" :key="slide.id">
          <div class="carousel__item2" @click="openModal(slide)">
            <img :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`" class="slideImg">
          </div>
        </Slide>
        <template #addons>
          <navigation />
        </template>
      </Carousel>
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
import { ref, onMounted, defineComponent } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { Carousel, Slide, Navigation } from 'vue3-carousel';
import MovieModal from '@/components/MovieModal.vue';
import "vue3-carousel/dist/carousel.css";

const store = useMovieStore();
const route = useRoute();

const slides = ref([]);
const isModalOpen = ref(false);
const currentSlide = ref({});
const isAutoplay = ref(1000); // Initial autoplay value in milliseconds

const fetchBoxOffice = async () => {
  await store.getBoxOffice();
  slides.value = store.boxOffice;
};

const openModal = (slide) => {
  currentSlide.value = slide;
  isModalOpen.value = true;
  isAutoplay.value = 0; // Stop the autoplay
};

const closeModal = () => {
  isModalOpen.value = false;
  isAutoplay.value = 1000; // Resume the autoplay
};

onMounted(() => {
  fetchBoxOffice();
});

defineComponent({
  name: 'BoxOffice',
  components: {
    Carousel,
    Slide,
    Navigation,
    MovieModal,
  },
});
</script>

<style scoped>
/* 기존 스타일 유지 */
.boxoffice-container {
  height: 45vh;
  display: flex;
  flex-direction: column;
}
.carousel-container2 {
  width: 100%;
}
.boxoffice-title {
  margin-top: 20px;
  margin-bottom: 20px;
  margin-left: 40px;
  font-size: 20px;
  align-self: flex-start;
  color: #eeeeee;
  font-weight: bold;
}
._cont2 {
  display: flex;
  justify-content: center;
  align-items: center;
}
.slideImg {
  width: 180px;
  height: 270px;
  cursor: pointer;
}
.carousel__item2 {
  width: 300px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}
strong {
  color: #0092ca;
  font-weight: bold;
}
</style>
