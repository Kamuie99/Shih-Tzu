<template>
  <main>
    <div height="92vh">
      <div v-if="loading">Loading...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else>
        <div class="main-container-big _2">
          <div class="profile-container2 _1">
            <div class="title-container-ranking">
              <img src="@/assets/images/podium.png" alt="">
              <p>이 달의 최고 <strong>인기쟁이</strong></p>
            </div>
            <div class="container-inner2">
              <div v-for="(user, index) in allUsers.slice(0, 3)" :key="user.id">
                <div class="inner-cont">
                  <h1 class="ranking-title">
                    <img :src="getMedalImage(index)" width="px" height="px" alt="">
                    <strong>|</strong>
                    <RouterLink :to="{name: 'profile', params: {username: user.username}}">
                      {{ user.username }}
                    </RouterLink> 의 컬렉션
                    <hr>
                    <!-- <strong> | </strong> -->
                    <!-- <p>{{ user.followers.length }}</p> -->
                  </h1>
                </div>
                <div class="inner-cont2">
                  <div v-if="user.liked_movies.length" class="collection-movies">
                    <img v-for="(movie, index) in user.liked_movies.slice(0, 3)" :key="index" :src="`https://image.tmdb.org/t/p/original${movie.backdrop_path}`" @click="openModal(movie)">
                  </div>
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
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useMovieStore } from '@/stores/movie';
import axios from 'axios'
import MovieModal from '@/components/MovieModal.vue';

const store = useMovieStore()

const allUsers = ref([])
const loading = ref(true)
const error = ref('')

const fetchLikedMovies = async () => {
  try {
    const response = await axios.get('http://localhost:8000/api/movies/ranking')
    allUsers.value = response.data
  } catch (err) {
    error.value = 'Failed to fetch liked movies. Please try again later.'
    console.error('Error fetching liked movies:', err)
  } finally {
    loading.value = false
  }
}

const isModalOpen = ref(false);
const currentSlide = ref({});

const openModal = (movie) => {
  currentSlide.value = movie;
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
};

const getMedalImage = (index) => {
  const medals = {
    0: new URL('@/assets/images/gold-medal.png', import.meta.url).href,
    1: new URL('@/assets/images/silver-medal.png', import.meta.url).href,
    2: new URL('@/assets/images/bronze-medal.png', import.meta.url).href
  };
  return medals[index];
};

onMounted(() => {
  fetchLikedMovies()
})
</script>

<style scoped>
.main-container-big {
  background-color: #1b1b1b;
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 100%;
}
.profile-container2 {
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  margin-top: 50px;
  width: 70%;
  max-width: 740px;
  min-height: 220px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 20px;
}
.container-inner2 {
  width: 100%;
  min-height: 210px;
  height: 100%;
  padding-top: 20px;
  display: flex;
  flex-direction: column;
  background-color: #eeeeee;
  border-radius: 10px;
  color: black;
}
.ranking-title {
  margin-left: 20px;
  align-items: center;
  display: flex;
  padding-right: 20px;
}
.ranking-title > a {
  text-decoration: none;
  color: #0092ca;
}
.ranking-title > strong {
  margin-left: 5px;
}
.ranking-title > p {
  margin-left: 10px;
}
.collection-movies {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  margin-left: 26px;
}
.collection-movies > img {
  width: 200px;
  margin-right: 20px;
  margin-bottom: 20px;
  cursor: pointer;
  border-radius: 30px;
}
.inner-cont {
  width: 100%;
  height: auto;
}
.inner-cont2 {
  width: 100%;
  height: auto;
  display: flex;
  /* justify-content: center; */
  align-items: center;
  margin-top: 20px;
}
.title-container-ranking {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
  margin-left: 10px;
}
.title-container-ranking > p {
  color: white;
  font-size: 19px;
  margin-left: 10px;
}
</style>
