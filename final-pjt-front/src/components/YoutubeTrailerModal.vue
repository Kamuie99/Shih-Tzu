<template>
  <div class="modal" v-if="videoId">
    <div class="modal-inner">
      <div class="title-button">
        <p class="title">공식 예고편</p>
        <button @click="$emit('close')">X</button>
      </div>
      <iframe width="560" height="315" :src="youtubeUrl" frameborder="0" allowfullscreen></iframe>
    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const props = defineProps({
  videoId: String
});

const youtubeUrl = computed(() => {
  return props.videoId ? `https://www.youtube.com/embed/${props.videoId}?modestbranding=1&rel=0&autoplay=1&iv_load_policy=3&cc_load_policy=1&fs=0&playsinline=1&showinfo=0&enablejsapi=1&origin=http://localhost:5173&widget_referrer=http://localhost:5173&privacy_mode=true` : '';
});


console.log(props.videoId)
</script>

<style scoped>
.modal {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.8);
}
.modal-inner {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 38rem;

  background-color: white;
  padding: 10px;
}

.title-button {
  width: 36rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding-left: 20px;
  padding-right: 20px;
  margin-bottom: 30px;
  align-items: center;
}

.title {
  font-weight: bold;
}
iframe {
  margin-bottom: 20px;
}
button {
  cursor: pointer;
  background-color: white;
  border: none;
  font-size: 20px;

  align-self: flex-end;
}
</style>