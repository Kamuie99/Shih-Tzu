<template>
  <div class="register-template">
    <div v-if="!authStore.isAuthenticated" class="register-container">
      <RouterLink to="/">
        <img src="@/assets/images/newLogo.png" id="logo-img">
      </RouterLink>
      <h2 class="register-title"><strong>시추</strong>에 오신 것을 환영합니다!</h2>
      <form class="register-form" @submit.prevent="registerSubmit" autocomplete="off">
        <div class="register-inner">
          <input type="text" v-model="username" placeholder="ShihTzu 아이디 또는 이메일" autocomplete="off" required>
        </div>
        <div class="register-inner">
          <input type="password" v-model="password1" placeholder="ShihTzu 비밀번호 설정" autocomplete="new-password" required>
        </div>
        <div class="register-inner">
          <input type="password" v-model="password2" placeholder="비밀번호 재확인" autocomplete="new-password" required>
        </div>
        <div :class="['error-message-container', { shake: shakeError }]">
          <!-- <p class="error-message" v-if="error">ⓘ비밀번호는 8~20자 이내로 영문, 숫자, 특수문자를 혼용하여 입력해 주세요.</p> -->
          <p class="error-message" v-if="error">ⓘ{{ error }}</p>
        </div>
        <button class="register-button" type="submit">Register</button>
        <p class="linktoLogin">이미 계정이 있으신가요? <RouterLink to="/login">로그인</RouterLink></p>
      </form>
    </div>
    <div v-else>
      <p>이미 로그인 되어있습니다.</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const router = useRouter()
const authStore = useAuthStore()

const username = ref('')
const password1 = ref('')
const password2 = ref('')
const error = ref('')
const shakeError = ref('')

const registerSubmit = async () => {
  if (password1.value.length < 8 || password1.value.length > 20) {
    error.value = '비밀번호는 8 ~ 20자리 입니다.'
    shakeError.value = true
    setTimeout(() => {
      shakeError.value = false
    }, 500)
    return
  }

  if (password1.value !== password2.value) {
    error.value = '두 비밀번호가 일치하지 않습니다.'
    shakeError.value = true
    setTimeout(() => {
      shakeError.value = false
    }, 500)
    return
  }


  try {
    await authStore.register(username.value, password1.value, password2.value)
    router.push('/')
    await this.login()
  } catch (err) {
    console.log(err)
    error.value = '이미 존재하는 ID입니다.'
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
.register-template {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #393E46;
}
.register-container {
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
#logo-img {
  width: 100px;
  height: 100px;
}
.register-title {
  margin-top: 20px;
}
.register-form {
  width: 100%;
  height: 60%;
  margin-top: 40px;
  
  display: flex;
  flex-direction: column;
  align-items: center;
}
.register-inner {
  width: 100%;
  height: 15%;
  text-align: center;
  margin-bottom: 20px;
}
.register-inner > input {
  width: 80%;
  height: 100%;
  background-color: #2F2F2F;
  color: #eeeeee;
  border-radius: 5px;
  border: 1px solid #2f2f2f;
  padding-left: 10px;
  box-shadow: 0 0 2px rgb(0, 0, 0.5);
}
.register-inner > input:-webkit-autofill {
  -webkit-box-shadow: 0 0 0px 1000px #2F2F2F inset;
  -webkit-text-fill-color: #eeeeee;
  transition: background-color 5000s ease-in-out 0s;
}
.register-button {
  width: 82.5%;
  height: 15%;
  background-color: #0092ca;
  color: #eeeeee;
  border: 1px solid #0092ca;
  border-radius: 20px;
  cursor: pointer;
}
.linktoLogin {
  font-size: 10px;
  color: lightgray;
  margin-top: 10px;
}
.linktoLogin > a {
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