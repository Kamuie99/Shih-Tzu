<template>
  <div class="profile-container2 _1">
    <div class="container-inner2">
      <div class="inner-cont">
        <h1 class="following-title"><strong>| {{ route.params.username }}</strong> 의 팔로잉 목록</h1>
      </div>
      <div class="inner-cont2">
        <div v-if="followings.length" class="following-peoples">
          <div class="tiny-profile" v-for="following in followings" :key="following.id">
            <div class="tiny-profile-image">
              <img v-if="following.profile_image" :src="`${API_URL}${following.profile_image}`" width="40px" height="40px" alt="">
              <img v-else src="@/assets/images/newLogo.png" width="40px" height="40px" alt="">
            </div>
            <div class="tiny-profile-name">
              <strong>| </strong> <RouterLink :to="{name: 'profile', params: {username: following.username }}"> {{ following.username }}</RouterLink>
            </div>        
          </div>
        </div>
        <div v-else>
          팔로우하는 사람이 없습니다
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const API_URL = 'http://localhost:8000'
const route = useRoute()
const store = useMovieStore()
const followings = computed(() => store.followings);
</script>

<style scoped>
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
.following-title {
  margin-left: 40px;
  font-size: 18px;
}
.following-peoples {
  width: 90%;
  height: auto;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.following-peoples > div {
  padding-left: 5px;
  border-radius: 5px;
  border: 1px solid #0092ca;
  width: 170px;
  height: 50px;
  margin-right: 20px;
  margin-bottom: 20px;
}
.tiny-profile {
  width: 100%;
  display: flex;
  flex-direction: row;
}
.tiny-profile-image {
  display: flex;
  justify-content: center;
  align-items: center;
}
.tiny-profile-name {
  width: 100px;
  display: flex;
  align-items: center;
  margin-left: 10px;
}
.tiny-profile-name > a {
  margin-left: 5px;
  text-decoration: none;
  color: #0092ca;
}
</style>