<template>
  <main>
    <div class="main-container-big _2">
      <form @submit.prevent="submitForm" class="searchForm">
        <div class="form-inner">
          <div class="input-container">
            <div class="input-titlecont">
              <label for="search-box" class="shihtzu-tinytitle"
                >영화 <strong>검색</strong></label
              >
              <select class="time-selectbox" v-model="selectedGenre">
                <option value="">모든 장르</option>
                <option
                  v-for="genre in genres"
                  :key="genre.id"
                  :value="genre.id"
                >
                  {{ genre.name }}
                </option>
              </select>
            </div>
            <div class="input-innercont">
              <div class="search-box">
                <input
                  id="search-box"
                  type="text"
                  placeholder="영화 제목으로 찾아보세요"
                  v-model="searchQuery"
                />
                <button type="submit" value="제출" class="buttonSubmit">
                  찾기
                </button>
              </div>
            </div>
          </div>
        </div>
      </form>
    </div>
    <div ref="bottomDiv">
      <div class="main-container _1">
        <div class="boxoffice-container">
          <p class="boxoffice-title"><strong>| 상영중</strong> 영화</p>
          <div v-if="nowPlayingMovies.length" class="carousel-container2">
            <Carousel
              :itemsToShow="5"
              :wrapAround="false"
              :transition="1000"
              :pauseAutoplayOnHover="true"
            >
              <Slide v-for="slide in nowPlayingMovies" :key="slide.id">
                <div class="carousel__item2" @click="openModal(slide)">
                  <img
                    :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`"
                    class="slideImg"
                  />
                </div>
              </Slide>
              <template #addons>
                <navigation />
              </template>
            </Carousel>
          </div>
          <div v-else class="main-container nothingSearch _1">
            <p>현재 상영중인 '{{ searchQuery }}' 영화가 없어요.</p>
          </div>
        </div>
      </div>

      <div class="main-container _3">
        <div class="boxoffice-container">
          <p class="boxoffice-title"><strong>| OTT</strong> 검색결과</p>
          <div v-if="notNowPlayingMovies.length" class="carousel-container2">
            <Carousel
              :itemsToShow="5"
              :wrapAround="false"
              :transition="1000"
              :pauseAutoplayOnHover="true"
            >
              <Slide v-for="slide in notNowPlayingMovies" :key="slide.id">
                <div class="carousel__item2" @click="openModal(slide)">
                  <img
                    :src="`https://image.tmdb.org/t/p/original${slide.poster_path}`"
                    class="slideImg"
                  />
                </div>
              </Slide>
              <template #addons>
                <navigation />
              </template>
            </Carousel>
          </div>
          <div v-else class="main-container nothingSearch _3">
            <p>'{{ searchQuery }}' 검색 결과가 없어요.</p>
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
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, defineComponent } from "vue";
import { useMovieStore } from "@/stores/movie";
import { Carousel, Slide, Navigation, Pagination } from "vue3-carousel";
import MovieModal from "@/components/MovieModal.vue";
import "vue3-carousel/dist/carousel.css";

const store = useMovieStore();

const genres = store.genres;
const nowPlayingMovies = ref([]);
const notNowPlayingMovies = ref([]);
const selectedGenre = ref("");
const searchQuery = ref("");
const bottomDiv = ref(null);

const isModalOpen = ref(false);
const currentSlide = ref({});
const isAutoplay = ref(1000); // Initial autoplay value in milliseconds

const submitForm = async () => {
  // if (!searchQuery.value) {
  //     alert('검색어를 입력해주세요')
  //     return
  // }
  const result = await store.searchMovies(
    searchQuery.value,
    selectedGenre.value
  );
  nowPlayingMovies.value = result.nowPlayingMovies;
  notNowPlayingMovies.value = result.notNowPlayingMovies;
  bottomDiv.value.scrollIntoView({ behavior: "smooth" });
};

const openModal = (slide) => {
  currentSlide.value = slide;
  isModalOpen.value = true;
  isAutoplay.value = 0; // Stop the autoplay
};

const closeModal = () => {
  isModalOpen.value = false;
  // isAutoplay.value = 1000; // Resume the autoplay
};

onMounted(() => {
  store.getGenres();
});

defineComponent({
  name: "SearchView",
  components: {
    Carousel,
    Slide,
    Navigation,
    MovieModal,
  },
});
</script>

<style scoped>
.main-container {
  height: 46vh;
}
.main-container-big {
  height: 92vh;
}
._1 {
  background-color: #252525;
}
._2 {
  background-image: url("@/assets/images/mainImg.png");
  background-color: rgba(0, 0, 0, 0.5);
}
._3 {
  background-color: #1b1b1b;
}
.searchForm {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  height: 100%;
}
.buttonSubmit {
  font-size: 30px;
  cursor: pointer;
  background-color: #393e46;
  border: none;
  transition: transform 0.3s ease-in-out;
}
.buttonSubmit:hover {
  transform: scale(1.15);
}
.form-inner {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.input-container {
  width: 60%;
  height: 80%;
  display: flex;
  flex-direction: column;
}
label svg {
  fill: #252525; /* 기본 색상 */
  transition: fill 0.3s ease-in-out;
  cursor: pointer;
}

label.selected svg {
  fill: #0092ca; /* 선택된 색상 */
}
.shihtzu-tinytitle {
  width: 150px;
  color: #eeeeee;
  font-size: 30px;
}
.input-innercont {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
}
.shihtzu-select {
  width: 60%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
}
.shihtzu-select > input {
  display: none;
}
.arrow-container {
  margin-top: 100px;
}
.input-titlecont {
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-top: 200px;
}
.time-selectbox {
  background-color: transparent;
  border: 1px solid #eeeeee;
  color: #eeeeee;
  border-radius: 10px;
  width: 200px;
  height: 50px;
  padding-left: 10px;
  font-size: 15px;
}
.time-selectbox > option {
  color: black;
}
.search-box {
  width: 100%;
  height: 80px;
  display: flex;
  align-items: center;
  margin-top: 50px;
}
.search-box > input {
  width: 850px;
  height: 75px;
  background-color: transparent;
  color: #eeeeee;
  border: 1px solid lightgray;
  border-radius: 10px;
  font-size: 20px;
  padding-left: 20px;

  -webkit-text-fill-color: #eeeeee; /* Set text color */
  transition: background-color 5000s ease-in-out 0s; /* Prevent autofill background change */
}
.search-box > button {
  margin-left: 20px;
  width: 150px;
  height: 100%;
  color: #eeeeee;
  background-color: #0092ca;
  border-radius: 10px;
}

/* Remove focus effect */
.search-box > input:focus,
.time-selectbox:focus,
.buttonSubmit:focus {
  outline: none;
  box-shadow: none;
  border: 1px solid #0092ca; /* or any other border style you want to keep */
}
.carousel-container2 {
  width: 100%;
}
.slideImg {
  width: 180px;
  height: 270px;
  cursor: pointer;
}
.boxoffice-container {
  height: 45vh;
  display: flex;
  flex-direction: column;
}
.boxoffice-title {
  margin-top: 30px;
  margin-bottom: 10px;
  margin-left: 40px;
  font-size: 20px;
  align-self: flex-start;
  color: #eeeeee;
  font-weight: bold;
}
.carousel__item2 {
  width: 300px;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.nothingSearch {
  display: flex;
  justify-content: center;
  align-items: center;
  color: #eeeeee;
  font-size: 20px;
}

/* Apply the same styling for autofilled input */
.search-box > input:-webkit-autofill {
  background-color: transparent !important;
  -webkit-text-fill-color: #eeeeee !important;
  transition: background-color 5000s ease-in-out 0s !important; /* Prevent autofill background change */
}
</style>
