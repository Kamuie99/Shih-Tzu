<template>
  <div class="profile-container2 _1">
    <div class="container-inner2">
      <div class="inner-cont">
        <h1 class="profileComments-title"><strong>| {{ route.params.username }} </strong> 의 코멘트</h1>
      </div>
      <div class="inner-cont2">
        <div v-if="formattedComments.length" class="commentsContainer">
          <div @click="openModal(comment.movie)" class="comment-card" v-for="comment in formattedComments" :key="comment.id">
            <div>
              <img :src="`https://image.tmdb.org/t/p/original${comment.movie.poster_path}`" width="100px">
            </div>
            <div class="comment-card-inner">
              <p class="comment-card-title"><strong>| </strong>{{ comment.movie.title }}</p>
              <p>{{ comment.formattedDate }}</p>
              <p>{{ comment.content }}</p>
            </div>
          </div>
        </div>
        <div v-else>
          첫 리뷰를 남겨보세요
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

const route = useRoute();
const store = useMovieStore();
const authstore = useAuthStore();

const comments = computed(() => store.comments);

const formatDate = (dateString) => {
  return dateString.replace('T', ' ').split('.')[0];
};

const formattedComments = computed(() => {
  return comments.value.map(comment => ({
    ...comment,
    formattedDate: formatDate(comment.created_at),
  }));
});

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
.inner-cont {
  width: 100%;
  height: auto;
}
.profileComments-title {
  margin-left: 40px;
  font-size: 18px;
}
.inner-cont2 {
  width: 100%;
  height: auto;
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
.comment-card {
  width: 80%;
  display: flex;
  flex-direction: row;
  margin-left: 30px;
  margin-bottom: 50px;
  padding: 10px;
  border-radius: 10px;
  border: 1px solid #0092ca;
  cursor: pointer;
}
.comment-card-inner {
  min-width: 50%;
  margin-left: 20px;
  flex-wrap: wrap;
}
.comment-card-inner > p {
  margin-bottom: 20px;
}
.comment-card-title {
  color: #0092ca;
}
.commentsContainer {
  width: 100%;
}
</style>
