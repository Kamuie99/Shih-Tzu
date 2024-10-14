<template>
  <div class="login-template">
    <div v-if="!authStore.isAuthenticated" class="login-container">
      <RouterLink to="/">
        <img src="@/assets/images/newLogo.png" id="logo-img">
      </RouterLink>
      <h2 class="login-title"><strong>시</strong>간으로 <strong>추</strong>천받는 <strong>시추</strong></h2>
      <form class="login-form" @submit.prevent="loginSubmit">
        <div :class="['error-message-container', { shake: shakeError }]">
          <p class="error-message" v-if="error">ⓘ해당 계정을 찾을 수 없습니다. ID, PW를 다시 확인해주세요.</p>
        </div>
        <div class="login-inner">
          <input type="text" v-model="username" placeholder="이메일 주소 또는 아이디" required>
        </div>
        <div class="login-inner">
          <input type="password" v-model="password" placeholder="비밀번호" required>
        </div>
        <button class="login-button" type="submit">Login</button>
        <p class="linktoRegister">아직 계정이 없으신가요? <RouterLink to="register">회원가입</RouterLink></p>
      </form>
    </div>
    <div v-else>
      <p>이미 로그인 되어있습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter, RouterLink } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password = ref('')
const error = ref('')
const shakeError = ref('')

const loginSubmit = async () => {
  try {
    await authStore.login(username.value, password.value)
    router.push('/')
  } catch (err) {
    error.value = true
    shakeError.value = true
    setTimeout(() => {
      shakeError.value = false
    }, 500)
  }
}
</script>

<style scoped>
@keyframes shake {
  0% { transform: translateX(0); }
  25% { transform: translateX(-5px); }
  50% { transform: translateX(5px); }
  75% { transform: translateX(-5px); }
  100% { transform: translateX(0); }
}
.shake {
  animation: shake 0.5s;
}
.login-template {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  background-color: #393E46;
}
.login-container {
  width: 30%;
  height: 60%;
  background-color: #252525;
  color: #eeeeee;
  border-radius: 20px;
  padding: 20px;
  
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.login-title {
  margin-top: 20px;
}
.login-form {
  width: 100%;
  height: 60%;
  margin-top: 40px;
  
  display: flex;
  flex-direction: column;
  align-items: center;
}
.login-inner {
  width: 100%;
  height: 15%;
  text-align: center;
  margin-bottom: 20px;
}
.login-inner > input {
  width: 80%;
  height: 100%;
  background-color: #2F2F2F;
  color: #eeeeee;
  border-radius: 5px;
  border: 1px solid #2f2f2f;
  padding-left: 10px;
  box-shadow: 0 0 2px rgb(0, 0, 0.5);
}
.login-inner > input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #2F2F2F inset;
  -webkit-text-fill-color: #eeeeee;
  transition: background-color 5000s ease-in-out 0s;
}
.login-button {
  width: 82.5%;
  height: 15%;
  background-color: #0092ca;
  color: #eeeeee;
  border: 1px solid #0092ca;
  border-radius: 20px;
  cursor: pointer;
}
#logo-img {
  width: 100px;
  height: 100px;
}
strong {
  font-weight: bold;
  color: #0092ca;
}
.linktoRegister {
  font-size: 10px;
  color: lightgray;
  margin-top: 10px;
}
.linktoRegister > a {
  color: lightgray;
}
.error-message {
  padding-left: 35px;
  font-size: 10px;
  color: #DC254D;
}
.error-message-container {
  align-self: flex-start;
  height: 20px;
}
</style>
