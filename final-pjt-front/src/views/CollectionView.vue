<template>
  <div class="profile-container2 _1">
    <div class="container-inner2">
      <div class="inner-cont">
        <h1 class="collection-title"><strong>| {{ route.params.username }} </strong> 의 컬렉션</h1>
      </div>
      <div class="inner-cont2">
        <div v-if="likedMovies.length" class="collection-movies">
          <img v-for="movie in likedMovies" :key="movie.id" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" @click="openModal(movie)">
        </div>
        <div v-else>
          아직 좋아요 표시한 작품이 없어요
        </div>
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
import { ref, computed } from 'vue';
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAuthStore } from '@/stores/auth';
import MovieModal from '@/components/MovieModal.vue';

const route = useRoute()
const store = useMovieStore();
const authstore = useAuthStore();

const likedMovies = computed(() => store.likedMovies);

const isModalOpen = ref(false);
const currentSlide = ref({});

const openModal = (movie) => {
  currentSlide.value = movie;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};
</script>

<style scoped>
.collection-title {
  margin-left: 40px;
  font-size: 18px;
}
.collection-movies {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.collection-movies > img {
  width: 210px;
  margin-right: 20px;
  margin-bottom: 20px;
  cursor: pointer;
  border-radius: 10px;
}
.inner-cont {
  width: 100%;
  height: auto;
}
.inner-cont2 {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
</style>
