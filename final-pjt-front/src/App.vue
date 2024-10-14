<template>
  <header>
    <nav class="header-navigation">
      <div class="header-logo">
        <RouterLink to="/">
          <img src="@/assets/images/newLogo.png" id="logo-img">
        </RouterLink>
        <div class="nav-bar">
          <RouterLink to="/" active-class="active-link">Home</RouterLink>
          <RouterLink to="/shihtzu" active-class="active-link">ShihTzu</RouterLink>
          <RouterLink to="/Search" active-class="active-link">Search</RouterLink>
          <RouterLink to="/cinema" active-class="active-link">Cinema</RouterLink>
          <RouterLink to="/ranking" active-class="active-link">Ranking</RouterLink>
          <div></div>
        </div>
      </div>
      <div class="search-login-conatiner nav-item">
        <div class="login-register" v-if="!authStore.isAuthenticated">
          <RouterLink to="/login">
            <button class="login-button">로그인</button>
          </RouterLink>
          <RouterLink to="/register">
            <button class="register-button">회원가입</button>
          </RouterLink>
        </div>
        <div class="login-register" v-else>
          <span class="user-name">
            <RouterLink :to="{name: 'profile', params: {username: authStore.user}}">{{ authStore.user }}</RouterLink>님, 환영합니다 !
          </span>
          <button class="logout-button" @click="logout">로그아웃</button>
        </div>
      </div>
    </nav>
  </header>
  <main style="background-color: #1b1b1b;">
    <RouterView />
  </main>

</template>

<script setup>
import { onMounted } from 'vue'
import { RouterLink, RouterView, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'
import { useMovieStore } from '@/stores/movie'

const authStore = useAuthStore()
const movieStore = useMovieStore()
const router = useRouter()

const logout = () => {
  authStore.logout(router);
}

onMounted(() => {
  movieStore.getMovies()
})

authStore.checkAuth()
</script>

<style scoped>
/* Main content styles */
header {
  position: sticky;
  top: 0;
  z-index: 2;
  width: 100%;
  display: flex;
  align-items: center;
  height: 8vh;
  background-color: #1b1b1b;
  border-bottom: 1px solid #393e46;
}

main {
  height: 92vh;
}

.header-navigation {
  width: 100%;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
}

.nav-item {
  width: 20%;
}

.header-logo {
  display: flex;
  flex-direction: row;
  width: 50%;
}

#logo-img {
  width: 50px;
  height: 50px;
}

.search-login-conatiner {
  width: 40%;
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
}

.nav-bar {
  width: 60%;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
  margin-left: 10px;
}

.nav-bar a {
  text-decoration: none;
  color: #eeeeee;
}

.user-name {
  color: white;
}

.user-name > a {
  color: white;
  cursor: pointer;
}

a.active-link {
  text-decoration: none;
  color: #0092ca; /* Change to blue when active */
}

.login-register {
  height: 70%;
  display: flex;
  align-items: center;
}

.login-register button {
  margin-left: 20px;
  cursor: pointer;
  border-radius: 10px;
  box-shadow: 0 0 10px rgb(0, 0, 0.5);
}

.login-button {
  background-color: #eeeeee;
  border: 1px solid #eeeeee;
  padding: 10px;
  color: #393e46;
}

.register-button {
  background-color: #0092ca;
  border: 1px solid #0092ca;
  padding: 10px;
  color: #eeeeee;
}

.logout-button {
  min-width: 53px;
  background-color: #eeeeee;
  border: 1px solid #eeeeee;
  padding: 10px;
  color: #393e46;
  margin-left: 20px;
  cursor: pointer;
  border-radius: 5px;
  box-shadow: 0 0 10px rgb(0, 0, 0.5);
}

.search-bar input {
  background-color: #222831;
  color: #eeeeee;
  border: 1px solid #eeeeee;
  border-radius: 5px;
  padding: 10px;
}
</style>
