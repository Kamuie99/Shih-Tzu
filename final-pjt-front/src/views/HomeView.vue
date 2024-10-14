<template>
  <div>
    <div class="main-container-big">
      <div class="text-overlay">
        <h1 class="main-title">Shih-Tzu</h1>
        <p class="sub-title">
          <span v-for="(char, index) in subTitle" :key="index" :style="{ animationDelay: index * 0.3 + 's' }" class="fade-in">
            {{ char }}
          </span>
        </p>
      </div>
      <img src="@/assets/images/mainImg.png" class="mainImg">
      <img src="@/assets/images/scroll.png" class="scroll-icon" @click="scrollToContent">
    </div>
    <div class="main-container _1" ref="content">
      <BoxOffice />
    </div>
    <div class="main-container _2">
      <RecommendPreview />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import BoxOffice from '@/components/BoxOffice.vue';
import RecommendPreview from '@/components/RecommendPreview.vue';

const content = ref(null);
const subTitle = '시간으로 추천영화'.split('');

const scrollToContent = () => {
  if (content.value) {
    content.value.scrollIntoView({ behavior: 'smooth' });
  }
};
</script>

<style scoped>
.main-container {
  height: 46vh;
}
.main-container-big {
  height: 92vh;
  background-color: #1b1b1b;
  position: relative;
}
._1 {
  background-color: #252525;
}
._2 {
  background-color: #1b1b1b;
}
.mainImg {
  width: 100%;
  height: 100%;
  opacity: 1;
}
.scroll-icon {
  width: 80px;
  height: 80px;
  position: absolute;
  top: 92%;
  left: 50%;
  transform: translate(-50%, -50%);
  cursor: pointer;
}
.text-overlay {
  position: absolute;
  top: 35%;
  left: 51%;
  transform: translate(-50%, -50%);
  text-align: center;
  color: #fff;
}
.main-title {
  font-size: 4em;
  font-weight: bold;
  letter-spacing: 0.1em;
  margin-bottom: 20px; /* 간격 조정 */
  animation: fadeIn 2s ease-in-out;
}
.sub-title {
  font-size: 1.5em;
  letter-spacing: 0.1em;
}
.fade-in {
  opacity: 0;
  animation: fadeIn 2s forwards;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
    transform: translateY(-20px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>
