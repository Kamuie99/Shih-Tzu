<template>
  <div v-if="isModalOpen" class="modal" @click="handleOutsideClick">
    <div class="modal-content" @click.stop>
      <span class="close" @click="closeModal">&times;</span>
      <div class="modal-title">
        <strong>| ChatGpt 4o</strong> with <strong>시추</strong>
      </div>
      <div class="modal-text">
        <div class="user-container">
          <div class="user-prompt">
            <p ref="userPromptText">{{ displayText }}</p>
          </div>
          <img class="user-image" src="@/assets/images/newLogo.png" alt="">
        </div>
        <div class="AI-container">
          <img class="AI-image" src="@/assets/images/GPTLogo.svg" alt="GPT Logo">
          <div class="AI-reply">
            <p v-if="!isLoading">{{ AIText }}</p>
            <p v-else class="loading-dots">
              <span>.</span><span>.</span><span>.</span>
            </p>
          </div>
        </div>
        <div v-if="!isLoading" class="user-container-bottom">
          <button class="close-bottom" @click="closeModal">지금 바로 확인해보기 !</button>
          <img class="user-image" src="@/assets/images/newLogo.png" alt="">
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, toRef, watch, nextTick } from 'vue'

const props = defineProps({
  isModalOpen: Boolean,
  AIText: String,
  prompt: String,
});

const emit = defineEmits(['closeModal']);

const isModalOpen = toRef(props, 'isModalOpen');
const displayText = ref('');
const isLoading = ref(true);

const closeModal = () => {
  emit('closeModal');
};

const handleOutsideClick = (event) => {
  if (event.target.classList.contains('modal')) {
    closeModal();
  }
};

const typeEffect = async (text) => {
  let i = 0;
  const speed = 75;
  displayText.value = '';

  const typeWriter = () => {
    if (i < text.length) {
      displayText.value += text.charAt(i);
      i++;
      setTimeout(typeWriter, speed);
    }
  };
  
  await nextTick();
  typeWriter();
};

watch(() => props.AIText, (newAIText) => {
  if (newAIText) {
    isLoading.value = false;
  } else {
    isLoading.value = true;
  }
});

watch(() => props.prompt, (newPrompt) => {
  typeEffect(newPrompt);
});

isLoading.value = !props.AIText;
typeEffect(props.prompt);
</script>

<style scoped>
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
.modal-title {
  text-align: left;
  margin: 20px;
  font-size: 20px;
}
.modal-content {
  background-color: rgba(255, 255, 255, 0.800);
  margin: auto;
  padding: 0;
  border-radius: 10px;
  width: 650px;
  min-height: 60%;
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
  color: black;
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
.modal-text {
  padding: 30px;
  color: black;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
.modal-text p {
  margin-bottom: 15px;
  text-align: left;
}
.user-container {
  width: 100%;
  display: flex;
  justify-content: space-between;
}
.user-prompt {
  display: flex;
  justify-content: flex-end;
  width: 90%;
  background-color: #EFE2CC;
  margin-bottom: 20px;
  border-radius: 20px;
  padding: 10px;
  position: relative;
}
.user-prompt::after {
  content: '';
  position: absolute;
  top: 80%;
  right: -0.01%;
  transform: translateY(-50%);
  border-width: 10px;
  border-style: solid;
  border-color: transparent #EFE2CC transparent transparent;
}
.user-image {
  width: 40px;
  height: 40px;
  padding: 3px;
  background-color: #EFE2CC;
  border-radius: 20px;
  align-self: flex-end;
  margin-left: 7px;
}
.AI-container {
  width: 100%;
  display: flex;
}
.AI-reply {
  display: flex;
  justify-content: flex-start;
  width: 90%;
  background-color: #DDDDDD;
  border-radius: 20px;
  padding: 10px;
  position: relative;
  margin-top: 10px;
  margin-bottom: 20px;
}
.AI-reply > p {
  line-height: 1.5;
}
.AI-reply::before {
  content: '';
  position: absolute;
  left: -0.01px;
  transform: translateY(-50%);
  border-width: 10px;
  border-style: solid;
  border-color: transparent transparent transparent #DDDDDD;
}
.AI-image {
  width: 40px;
  height: 40px;
  padding: 3px;
  margin-right: 7px;
  background-color: #DDDDDD;
  border-radius: 20px;
}
.loading-dots {
  display: flex;
  justify-content: center;
  align-items: center;
}
.loading-dots span {
  animation: bounce 1.4s infinite;
  font-size: 24px;
  color: black;
  margin: 0 2px;
}
.loading-dots span:nth-child(1) {
  animation-delay: -0.32s;
}
.loading-dots span:nth-child(2) {
  animation-delay: -0.16s;
}
@keyframes bounce {
  0%, 80%, 100% {
    transform: scale(0);
  }
  40% {
    transform: scale(1);
  }
}
.user-container-bottom{
  width: 100%;
  display: flex;
  justify-content: end;
}
.close-bottom {
  font-size: 15px;
  background-color: #EFE2CC;
  border: none;
  box-shadow: rgb(0, 0, 0, 0.5);
  border-radius: 20px;
  animation: pulse 1.5s infinite;
}
@keyframes pulse {
  0% {
    background-color: #EFE2CC;
  }
  50% {
    background-color: #f3c94b;
  }
  100% {
    background-color: #EFE2CC;
  }
}
.close-bottom:hover,
.close-bottom:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}
</style>