<template>
  <div class="profile-container2 _1">
    <div class="container-inner2">
      <div class="inner-cont">
        <form class="profile-form" @submit.prevent="updateSubmit">
          <div class="change-title">
            <p>| 프로필 이미지 변경</p>
          </div>
          <div class="changeImage">
            <div class="ImageContainer">
              <img v-if="profileImageUrl" :src="profileImageUrl" width="200px" height="200px" alt="현재이미지">
              <img v-else src="@/assets/images/newLogo.png" alt="">
            </div>
            <input class="fileInput" type="file" @change="onFileChange" accept="image/*">
          </div>
          <button type="submit" class="submitChangeButton">저장</button>
        </form>
        <form class="profile-form" @submit.prevent="changePasswordSubmit">
          <div class="change-title">
            <p>| 비밀번호 변경</p>
          </div>
          <div class="change-inputs">
            <input v-model="currentPassword" type="password" placeholder="현재 비밀번호">
            <input v-model="newPassword1" type="password" placeholder="새 비밀번호">
            <input v-model="newPassword2" type="password" placeholder="새 비밀번호 확인">
          </div>
          <button type="submit" class="submitChangeButton">변경</button>
        </form>
      </div>
      <div class="inner-cont2">
        <button type="button" class="userDeleteButton" @click.prevent="deleteUser()">회원 탈퇴</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth';
import { useRoute, useRouter } from 'vue-router';

const authStore = useAuthStore()
const route = useRoute()
const router = useRouter()

const file = ref(null)
const currentPassword = ref('')
const newPassword1 = ref('')
const newPassword2 = ref('')
const loading = ref(false)
const error = ref('')
const profileImageUrl = ref(route.query.profileImageUrl)


const onFileChange = (event) => {
  file.value = event.target.files[0]
}

const updateSubmit = async () => {
  const formData = new FormData()
  if (file.value) {
    formData.append('image', file.value)
  }
  try {
    await authStore.updateProfile(formData)
    alert('프로필이 성공적으로 업데이트 되었습니다.')
    window.history.back()
    setTimeout(() => {
      window.location.reload()
    }, 100);
  } catch (error) {
    console.error('업데이트 실패:', error)
    alert('프로필이 업데이트에 실패했습니다.')
  } 
}

const changePasswordSubmit = async () => {
  loading.value = true
  error.value = ''
  try {
    await authStore.changePassword(currentPassword.value, newPassword1.value, newPassword2.value)
    alert('비밀번호가 성공적으로 변경되었습니다.')
    window.history.back()
  } catch (err) {
    error.value = err.message
    alert(error.value)
  } finally {
    loading.value = false
  }
}

const deleteUser = async () => {
  const userConfirmed = confirm('삭제한 계정 정보는 되돌릴 수 없습니다. 정말 삭제하시겠습니까?')
  if (userConfirmed) {
    try {
      await authStore.deleteUser(authStore.user)
      alert('삭제되었습니다.')
      await authStore.logout(router)
      window.location.href = '/'
    } catch (err) {
      alert('삭제에 실패했습니다.' + err.message)
    }
  } else {
    alert('삭제를 취소했습니다.')
  }
}
</script>

<style scoped>
.change-title {
  color: #0092ca;
  font-weight: bold;
  margin-bottom: 40px;
}
.inner-cont {
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  padding-top: 40px;
  padding-bottom: 25px;
}
.change-inputs {
  display: flex;
  flex-direction: column;
  width: 30%;
}
.change-inputs > input {
  margin-bottom: 10px;
  border-radius: 5px;
  border: 1px solid #0092ca;
  width: 250px;
  height: 30px;
}
.profile-form {
  width: 40%;
}
.changeImage {
  display: flex;
  flex-direction: row;
  align-items: flex-end;
}
.ImageContainer {
  width: 130px;
  height: 130px;
  display: flex;
  justify-content: center;
  align-items: center;
  border: 1px solid #0092ca;
  border-radius: 5px;
}
.ImageContainer > img {
  width: 130px;
  height: 130px;
  border-radius: 5px;
}
.fileInput {
  margin-left: 20px;
}
#file-upload-button {
  background-color: transparent;
  border: 1px solid #0092ca;
}
.submitChangeButton {
  width: 257px;
  margin-top: 20px;
  background-color: #0092ca;
  border: 1px solid #0092ca;
  color: white;
  border-radius: 5px;
  cursor: pointer;
}
.inner-cont2 {
  margin-top: 0px;
  padding-bottom: 20px;
  width: 100%;
  text-align: right;
}
.userDeleteButton {
  background-color: red;
  color: white;
  width: 100px;
  border-radius: 5px;
  border: 1px solid red;
  cursor: pointer;
  margin-right: 30px;
}
</style>