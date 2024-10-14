<template>
  <div v-if="isModalOpen" class="modal" @click="handleOutsideClick">
    <div class="modal-content" @click.stop>
      <span class="close" @click="closeModal">&times;</span>
      <div class="image-container">
        <iframe 
          v-if="videoId" 
          :src="youtubeUrl" 
          frameborder="0" 
          allowfullscreen
          class="modal-video">
        </iframe>
        <div v-else class="modal-img">
          <img :src="`https://image.tmdb.org/t/p/original${currentSlide.backdrop_path}`" class="modal-img">
        </div>
        <div class="image-overlay"></div>
      </div>
      <div class="modal-text">
        <p class="currentSlide-title">
          {{ currentSlide.title }}
          <button id="like-button" @click.prevent="toggleLike(currentSlide.id)">
            <p v-if="isLiked">❤️</p>
            <p v-else>🤍</p>
          </button>
        </p>
        <div class="date-score">
          <p class="modal-tiny-title">개봉일 <strong>|</strong> {{ currentSlide.released_date }}</p>
          <p class="modal-tiny-title">평점 <strong>|</strong> {{ currentSlide.vote_avg }}</p>
        </div>
        <p class="currentSlide-aboutMovie">{{ currentSlide.overview }}</p>
      </div>

      <div class="related-movies">
        <div class="modal-text">
          <p class="modal-tiny-title">관련 영화 <strong>|</strong></p>
        </div>
        <div class="modal-carousel">
          <Carousel :itemsToShow="3" :wrapAround="false" :transition="500">
            <Slide v-for="movie in similarMovies" :key="movie.id">
              <div class="carousel__item2" @click="selectMovie(movie)">
                <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" width="100px" alt="">
              </div>
            </Slide>
            <template #addons>
              <Navigation/>
            </template>
          </Carousel>
        </div>
        <!-- <div style="color: white;" v-for="movie in similarMovies">
          <img :src="`https://image.tmdb.org/t/p/original${movie.poster_path}`" width="100px" alt="">
        </div> -->
      </div>

      <div class="modal-text">
        <div class="comment-title-input">
          <p class="comment-tiny-title">리뷰 <strong>|</strong></p>
          <!-- 지우야 여기야 댓글작성은 여기에! -->
          <div class="comment-write">
            <form class="input-comment" @submit.prevent="commentSubmit(currentSlide.id)">
              <textarea maxlength="200" v-model="commentText" @keyup.enter="submitForm"></textarea>
              <input type="submit" value="작성">
            </form>
          </div>
        </div>

        <!-- 지우야 여기야 댓글목록은 여기에! -->
        <div class="comments-container" v-if="commentStore.comments.length">
          <div class="user-comment" v-for="comment in commentStore.comments" :key="comment.id">
            <p class="comment-user"><strong><RouterLink :to="{name: 'profile', params: {username: comment.username}}">
              {{ comment.username }}
            </RouterLink> |</strong></p>
            <p class="comment-about">{{ comment.content }}</p>
            <button class="comment-delete-button" v-if="comment.username === authStore.user" @click.prevent="commentDelete(currentSlide.id, comment.id)">X</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, toRef, computed, onMounted } from 'vue';
import axios from 'axios';
import { useMovieStore } from '@/stores/movie';
import { useAuthStore } from '@/stores/auth';
import { useCommentStore } from '@/stores/comments';
import { Carousel, Slide, Navigation } from 'vue3-carousel';
import "vue3-carousel/dist/carousel.css";

const store = useMovieStore()
const authStore = useAuthStore()
const commentStore = useCommentStore()

const props = defineProps({
  isModalOpen: Boolean,
  currentSlide: Object,
});

const emit = defineEmits(['closeModal', 'movieSelected']);

const showModal = ref(false);
const videoId = ref(null);
const similarMovies = ref([]);
const isLiked = ref(false);
const commentText = ref('');
const isModalOpen = toRef(props, 'isModalOpen');

const youtubeUrl = computed(() => {
  return videoId.value ? `https://www.youtube.com/embed/${videoId.value}?autoplay=1&modestbranding=1&rel=0&iv_load_policy=3&controls=0` : '';
});

const closeModal = () => {
  emit('closeModal');
};

const handleOutsideClick = (event) => {
  if (event.target.classList.contains('modal')) {
    closeModal();
  }
};

const youtubeApiKey = import.meta.env.VITE_APP_YOUTUBE_API_KEY;
const searchUrl = import.meta.env.VITE_APP_YOUTUBE_API_URL;

const fetchYoutubeTrailer = async (movieTitle) => {
  try {
    const response = await axios.get(searchUrl, {
      params: {
        part: 'snippet',
        q: `${movieTitle} official trailer`,
        type: 'video',
        key: youtubeApiKey,
      },
    });
    if (response.data.items.length > 0) {
      videoId.value = response.data.items[0].id.videoId;
      showModal.value = true;
    }
  } catch (error) {
    console.error('Error:', error);
  }
};

const fetchSimilarMovies = async (movieId) => {
  try {
    const similarMoviesData = await store.getSimilarMovies(movieId)
    similarMovies.value = similarMoviesData;
  } catch (error) {
    console.error('Error fetching similar Movies:', error);
  }
};

const checkLiked = async (movieId) => {
  try {
    const liked = await store.checkLiked(movieId);
    isLiked.value = liked;
  } catch (error) {
    console.error('Error checking if movie is liked:', error);
  }
};

const toggleLike = async (movieId) => {
  try {
    const liked = await store.toggleLike(movieId)
    isLiked.value = liked
    const message = liked
      ? `${authStore.user} 님의 컬랙션에 저장되었습니다`
      : `${authStore.user} 님의 컬랙션에서 삭제되었습니다`;
    alert(message);
  } catch (error) {
    console.error('Error toggling like:', error);
  }
}

const selectMovie = (movie) => {
  emit('movieSelected', movie);
};

const commentSubmit = async (movieId) => {
  try {
    await commentStore.commentSubmit(movieId, commentText.value)
    commentText.value = ''
  } catch (error) {
    console.error('Error submitting comment:', error);
  }
}

const submitForm = () => {
  commentSubmit(props.currentSlide.id);
};

const commentDelete = async (movieId, commentId) => {
  try {
    await commentStore.commentDelete(movieId, commentId)
  } catch (error) {
    console.error('Error deleting comment:', error)
  }
}

watch([isModalOpen, () => props.currentSlide.id], async (newValue) => {
  const [modalOpen, movieId] = newValue
  if (modalOpen && movieId) {
    await fetchYoutubeTrailer(props.currentSlide.title);
    await fetchSimilarMovies(movieId);
    await checkLiked(movieId);
    await commentStore.getComments(movieId);
  } else {
    videoId.value = null;
    showModal.value = false;
  }
});

</script>

<style>
/* 기존 스타일 유지 */
.modal {
  display: flex;
  justify-content: center;
  align-items: center;
  position: fixed;
  border-radius: 10px;
  z-index: 2000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0,0,0,0.8); /* Darker background */
}
.modal-content {
  background-color: black;
  margin: auto;
  padding: 0;
  border-radius: 10px;
  width: 650px;
  min-height: 80%;
  text-align: center;
  animation: modalopen 0.5s;
  position: relative;
}
@keyframes modalopen {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}
.close {
  z-index: 2000;
  color: #eeeeee;
  position: absolute;
  top: 0px;
  right: 10px;
  font-size: 28px;
  font-weight: bold;
  cursor: pointer;
}
.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
.image-container {
  position: relative;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
}
.modal-video {
  width: 100%;
  height: 450px; /* Adjust this value to change the height */
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
}
.modal-img {
  width: 100%;
  height: auto;
  border-top-right-radius: 10px;
  border-top-left-radius: 10px;
}
.image-overlay {
  position: absolute;
  bottom: 0;
  width: 100%;
  height: 30%;
  background: linear-gradient(to top, rgba(0,0,0,1), rgba(0,0,0,0));
}
.modal-text {
  padding: 20px;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.modal-text > p {
  margin-bottom: 15px;
}
.currentSlide-title {
  display: flex;
  align-items: center;
  font-size: 20px;
  font-weight: bold;
}
.currentSlide-aboutMovie {
  text-align: left;
  line-height: 1.3;
}
.date-score {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  margin-bottom: 20px;
}
.modal-tiny-title {
  width: 50%;
  text-align: left;
}
strong {
  color: #0092ca;
  font-weight: bold;
}
.modal-carousel {
  padding-bottom: 20px;
}
.carousel__item2 {
  width: 100px;
  height: auto;
  cursor: pointer;
}
#like-button {
  background-color: black;
  border: none;
  width: 30px;
  height: 30px;
  display: flex;
  align-items: center;
  cursor: pointer;
}
#like-button > p {
  width: 20px;
  height: 20px;
}
.comments-container {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.user-comment {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  align-items: flex-start;
  margin-bottom: 15px;
  word-break: break-word; /* Add this line */
}
.comment-user {
  width: 15%;
  text-align: left;
}
.comment-about {
  width: 80%;
  text-align: left;
  line-height: 1.3;
  word-wrap: break-word; /* Add this line */
}
.comment-title-input {
  width: 100%;
  display: flex;
  flex-direction: row;
  align-items: center;
  margin-bottom: 20px;
}
.comment-title-input > input {
  margin-left: 20px;
}
.input-comment {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
.input-comment > textarea {
  padding-top: 10px;
  padding-left: 10px;
  width: 87%;
  height: 45px;
  border: 1px solid #0092CA;
  border-radius: 10px;
  resize: none;
  background-color: #000000;
  color: #eeeeee;
  outline: none;
}
.input-comment> input {
  width: 10%;
  height: 100%;
  border: none;
  border-radius: 10px;
  color: #eeeeee;
  background-color: #0092ca;
  cursor: pointer;
}
.comment-write {
  width: 550px;
  height: 50px;
  margin-left: 10px;
}
.comment-tiny-title {
  width: 50px;
}
.comment-user a {
  text-decoration: none;
  color: #0092CA;
}
.comment-delete-button {
  background-color: transparent;
  border: none;
  color: white;
  cursor: pointer;
}
</style>
