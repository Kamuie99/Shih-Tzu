<template>
  <div v-if="loading">Loading...</div>
  <div v-else-if="error">{{ error }}</div>
  <div v-else>
    <div class="main-container-big _2">
      <div class="profile-container1 _1">
        <div class="container-inner1">
          <div class="profileImage-container">
            <img v-if="profileImageUrl" :src="profileImageUrl" alt="">
            <img v-else src="@/assets/images/newLogo.png" alt="">
          </div>
          <div class="profileText-container">
            <div class="name-button">
              <p>
                <strong>{{ profile.username }}</strong>
              </p>
              <button v-if="!isOwnProfile" @click.prevent="toggleFollow">
                <p v-if="isFollowed">언팔로우</p>
                <p v-else>팔로우</p>
              </button>
              <RouterLink :to="{name: 'update', params: { username: profile.username}, query: { profileImageUrl: profileImageUrl }}" active-class="active-link" v-else class="profile-update-btn">
                <img src="@/assets/images/pencil.png" style="width: 16px;" alt="">
              </RouterLink>
            </div>

            <div class="profile-inner">
              <RouterLink :to="{ name: 'follower', params: { username: profile.username }}" active-class="active-link" @click.prevent="setFollower(profile.followers)">
                팔로워 <strong>|</strong> {{ profile.followers.length }}
              </RouterLink>
              <RouterLink :to="{ name: 'following', params: { username: profile.username }}" active-class="active-link" @click.prevent="setFollowing(profile.following)">
                팔로잉 <strong>|</strong> {{ profile.following.length }}
              </RouterLink>
            </div>
            <div class="profile-inner">
              <RouterLink :to="{ name: 'profilecomments', params: { username: profile.username }}" active-class="active-link" @click.prevent="setComments(profile.reviews)">
                코멘트 <strong>|</strong> {{ profile.reviews.length }}
              </RouterLink>
              <RouterLink :to="{ name: 'collection', params: { username: profile.username }}" active-class="active-link" @click.prevent="setLikedMovies(profile.liked_movies)">
                컬렉션 <strong>|</strong> {{ profile.liked_movies.length }}
              </RouterLink>
            </div>
          </div>
        </div>
      </div>
      <RouterView/>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useRoute, useRouter, RouterView, RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { useAuthStore } from '@/stores/auth';

const route = useRoute();
const router = useRouter();
const movieStore = useMovieStore();
const authStore = useAuthStore();

const profile = ref(null);
const profileImageUrl = ref(null)
const loading = ref(true);
const error = ref('');
const isFollowed = ref(false);
const isOwnProfile = ref(false);
const API_URL = 'http://localhost:8000'

const fetchProfile = async (username) => {
  try {
    const response = await authStore.profile(username);
    profile.value = response;
    profileImageUrl.value = profile.value.profile_image ? `${API_URL}${profile.value.profile_image}` : null;
    await checkFollowed(username)
  } catch (err) {
    error.value = 'Failed to fetch profile. Please try again later.';
    console.error('Error fetching profile:', err);
  } finally {
    loading.value = false;
  }
};

const setFollower = (followers) => {
  movieStore.followers = followers || []
}

const setFollowing = (following) => {
  movieStore.followings = following || []
}

const setComments = (comments) => {
  movieStore.comments = comments || []
}
const setLikedMovies = (movies) => {
  movieStore.likedMovies = movies || []
}

const checkFollowed = async (username) => {
  try {
    const follow = await authStore.checkFollowed(username);
    isFollowed.value = follow;
  } catch (error) {
    console.error('Error checking followed:', error);
  }
};

const toggleFollow = async () => {
  try {
    const follow = await authStore.toggleFollow(route.params.username)
    isFollowed.value = follow
    if (!profile.value.followers) {
      profile.value.followers = [];
    }
    if (follow) {
      profile.value.followers.push(authStore.userInfo)
    } else {
      profile.value.followers = profile.value.followers.filter(follower => follower.username !== authStore.user) || [];
    }
    window.location.reload();
  } catch (error) {
    console.error('Error toggling follow:', error);
  }
};

onMounted(() => {
  const username = route.params.username;
  if (username) {
    fetchProfile(username);
    isOwnProfile.value = (username === authStore.user)
  } else {
    loading.value = false;
    error.value = 'No username found.';
  }
});

watch(() => route.params.username, (newUsername) => {
  if (newUsername) {
    fetchProfile(newUsername);
    isOwnProfile.value = newUsername === authStore.user;
  }
});

watch(() => movieStore.followers, (newFollowers) => {
  movieStore.followers.value = newFollowers || [];
});

watch(isFollowed, (newVal) => {
});
</script>

<style>
._1 {
  background-color: #252525;
}
._2 {
  background-color: #1b1b1b;
}
._3 {
  background-color: #eeeeee;
}
.main-container-big {
  background-color: #1b1b1b;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.profile-container1 {
  width: 50%;
  min-width: 800px;
  height: 120px;
  margin-top: 50px;
  border-top-left-radius: 10px;
  border-top-right-radius: 10px;
  padding: 20px;
}
.profile-container2 {
  width: 50%;
  min-width: 800px;
  min-height: 200px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 20px;
}
.container-inner1 {
  width: 100%;
  height: 100%;

  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: #eeeeee;
  border-radius: 10px;

  color: black;
}
.container-inner2 {
  width: 100%;
  min-height: 200px;
  height: 100%;
  padding-top: 20px;

  display: flex;
  flex-direction: column;
  background-color: #eeeeee;
  border-radius: 10px;

  color: black;
}
.likes-comments {
  width: 50%;
  height: 400px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
  padding: 20px;
  padding-top: 0px;
}
.profileImage-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 20%;
}
.profileImage-container > img {
  width: 100px;
  height: 100px;
  border-radius: 50%;
}
.profileText-container{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 20px;
  width: 70%;
  color: black;
  font-size: 17px;
}
.profile-inner {
  display: flex;
  flex-direction: row;
  width: 170px;
  justify-content: space-between;
}
.profile-inner > a {
  text-decoration: none;
  color: black;
}
a.active-link {
  text-decoration: none;
  color: #0092ca; /* Change to blue when active */
  font-weight: bold;
}
.name-button {
  display: flex;
  flex-direction: row;
  align-items: center;
}
.name-button > button {
  margin-left: 10px;
  border-radius: 5px;
  border: 1px solid #0092ca;
  cursor: pointer;
}
.name-button > a {
  margin-left: 10px;
  color: #0092ca;
}
</style>