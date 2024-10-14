<template>
  <main>
    <div class="main-container-big _2">
      <form @submit.prevent="submitForm" class="searchForm">
        <div class="form-inner">
          <div class="input-container">
            <div class="input-titlecont">
              <h1 class="shihtzu-tinytitle"><strong>| {{ authstore.user }}</strong>님만을 위한 <strong>시</strong>간별 <strong>추</strong>천영화</h1>
              <select class="time-selectbox" v-model="store.selectedOption">
                <option value="now">현재 시간으로 추천받기</option>
                <option value="right">평일 저녁으로 추천받기</option>
                <option value="left">주말 오후로 추천받기</option>
              </select>
              
              
              <!-- partial:index.partial.html -->
              <div class="switch">
                <input type="checkbox" name="toggle" v-model="AIToggle">
                <label for="toggle">
                  <i class="bulb">
                    <span class="bulb-center"></span>
                    <span class="filament-1"></span>
                    <span class="filament-2"></span>
                    <span class="reflections">
                      <span></span>
                    </span>
                    <span class="sparks">
                      <i class="spark1"></i>
                      <i class="spark2"></i>
                      <i class="spark3"></i>
                      <i class="spark4"></i>
                    </span>
                  </i>    
                </label>
              </div>
              <div class="about-gpt">
                <p><strong>Gpt4</strong> with <strong>시추</strong></p>
              </div>
            </div>
            <div class="input-innercont">
              <div class="shihtzu-tinytitle where-who">Where? <strong>{{ where }}</strong></div>
              <div class="shihtzu-select">
                <input type="radio" v-model="where" name="where" value="Theater" id="Theater"/>
                <label for="Theater" :class="{ selected: where === 'Theater' }">
                  <svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24">
                    <path d="m19,0H5C2.243,0,0,2.243,0,5v15c0,2.243,1.792,4,4.08,4h1.913c.6,0,1.165-.265,1.55-.727.374-.448.53-1.03.427-1.598-.51-2.803-2.565-5.034-4.225-6.431,2.6-1.006,6.453-3.28,8.257-8.196,1.803,4.917,5.656,7.19,8.257,8.196-1.661,1.396-3.715,3.627-4.225,6.431-.103.567.053,1.149.427,1.598.385.462.95.727,1.55.727h1.913c2.288,0,4.08-1.757,4.08-4V5c0-2.757-2.243-5-5-5ZM5.992,22h-1.913c-1.166,0-2.08-.879-2.08-2v-3.592c1.469,1.147,3.55,3.156,3.992,5.592Zm-3.992-8.246V5c0-1.654,1.346-3,3-3h1.961c-.185,2.485-1.07,4.487-2.643,5.958-.404.377-.425,1.01-.048,1.413.197.211.463.317.73.317.245,0,.49-.089.683-.27,1.988-1.857,3.082-4.354,3.277-7.419h2.014c-.44,8.447-6.416,11.032-8.973,11.754ZM13.027,2h2.014c.195,3.065,1.289,5.561,3.277,7.419.193.181.438.27.683.27.267,0,.534-.106.73-.317.377-.403.356-1.036-.048-1.413-1.574-1.471-2.459-3.473-2.643-5.958h1.961c1.654,0,3,1.346,3,3v8.759c-2.558-.71-8.536-3.274-8.973-11.759Zm8.973,18c0,1.121-.914,2-2.08,2l-1.921.033c.447-2.456,2.531-4.474,4.001-5.624v3.591Z"/>
                  </svg>
                </label>
                <input type="radio" v-model="where" name="where" value="Home" id="Home"/>
                <label for="Home" :class="{ selected: where === 'Home' }">
                  <svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px" viewBox="0 0 24 24"><g id="_01_align_center" data-name="01 align center"><path d="M13.338.833a2,2,0,0,0-2.676,0L0,10.429v10.4a3.2,3.2,0,0,0,3.2,3.2H20.8a3.2,3.2,0,0,0,3.2-3.2v-10.4ZM15,22.026H9V17a3,3,0,0,1,6,0Zm7-1.2a1.2,1.2,0,0,1-1.2,1.2H17V17A5,5,0,0,0,7,17v5.026H3.2a1.2,1.2,0,0,1-1.2-1.2V11.319l10-9,10,9Z"/></g></svg>
                </label>
              </div>
            </div>
            <div class="input-innercont">
              <h1 class="shihtzu-tinytitle where-who">Who? <strong>{{ withWho }}</strong></h1>
              <div class="shihtzu-select">
                <input type="radio" v-model="withWho" name="withWho" value="Alone" id="Alone"/>
                <label for="Alone" :class="{ selected: withWho === 'Alone' }">
                  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="100" height="100"><g id="_01_align_center" data-name="01 align center"><path d="M21,24H19V18.957A2.96,2.96,0,0,0,16.043,16H7.957A2.96,2.96,0,0,0,5,18.957V24H3V18.957A4.963,4.963,0,0,1,7.957,14h8.086A4.963,4.963,0,0,1,21,18.957Z"/><path d="M12,12a6,6,0,1,1,6-6A6.006,6.006,0,0,1,12,12ZM12,2a4,4,0,1,0,4,4A4,4,0,0,0,12,2Z"/></g></svg>
                </label>
                <input type="radio" v-model="withWho" name="withWho" value="Friend" id="Friend"/>
                <label for="Friend" :class="{ selected: withWho === 'Friend' }">
                  <svg id="Layer_1" height="100" viewBox="0 0 24 24" width="100" xmlns="http://www.w3.org/2000/svg" data-name="Layer 1"><path d="m7.5 13a4.5 4.5 0 1 1 4.5-4.5 4.505 4.505 0 0 1 -4.5 4.5zm0-7a2.5 2.5 0 1 0 2.5 2.5 2.5 2.5 0 0 0 -2.5-2.5zm7.5 17v-.5a7.5 7.5 0 0 0 -15 0v.5a1 1 0 0 0 2 0v-.5a5.5 5.5 0 0 1 11 0v.5a1 1 0 0 0 2 0zm9-5a7 7 0 0 0 -11.667-5.217 1 1 0 1 0 1.334 1.49 5 5 0 0 1 8.333 3.727 1 1 0 0 0 2 0zm-6.5-9a4.5 4.5 0 1 1 4.5-4.5 4.505 4.505 0 0 1 -4.5 4.5zm0-7a2.5 2.5 0 1 0 2.5 2.5 2.5 2.5 0 0 0 -2.5-2.5z"/></svg>
                </label>
                <input type="radio" v-model="withWho" name="withWho" value="Family" id="Family"/>
                <label for="Family" :class="{ selected: withWho === 'Family' }">
                  <svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24">
                    <path d="m24,7v12.231c0,.742-.273,1.455-.772,2.01l-2.489,2.759h-2.693l3.697-4.098c.166-.185.258-.423.258-.671V7c0-.551-.449-1-1-1s-1,.449-1,1v8h-.005c0,.684-.232,1.369-.696,1.922l-2.578,2.684-1.441-1.386,2.533-2.634c.448-.471.087-1.084-.066-1.255-.366-.409-.998-.443-1.406-.077l-2.908,2.676c.366.507.568,1.122.568,1.756v5.314h-2v-5.314c0-.279-.118-.547-.323-.735l-4.026-3.705c-.398-.356-1.03-.324-1.397.086-.328.367-.337.928-.021,1.305l2.57,2.671-1.441,1.386-2.616-2.721c-.488-.579-.73-1.279-.735-1.972h-.011V7c0-.551-.449-1-1-1s-1,.449-1,1v12.231c0,.248.092.486.258.671l3.697,4.098h-2.693l-2.489-2.759c-.499-.555-.772-1.268-.772-2.01V7c0-1.654,1.346-3,3-3,1.053,0,1.98.546,2.516,1.369.263-.229.607-.369.984-.369h1.5c0,.618.147,1.198.401,1.717-.766.58-1.278,1.462-1.369,2.471v.815c-.346-.002-.692.031-1.032.1v2.068c.999-.35,2.153-.161,2.996.594l3.004,2.764,2.995-2.756c.849-.761,2.007-.951,3.005-.602v-2.065c-.34-.068-.687-.101-1.034-.098v-.842c-.096-1-.606-1.874-1.367-2.45.253-.519.401-1.099.401-1.717h1.5c.377,0,.721.139.984.369.535-.823,1.463-1.369,2.516-1.369,1.654,0,3,1.346,3,3Zm-10.5,1h-3c-.828,0-1.5.672-1.5,1.5v.919c.474.207.924.492,1.33.855l1.67,1.536,1.64-1.51c.416-.372.876-.663,1.36-.874v-.928c0-.828-.672-1.5-1.5-1.5Zm-5.5-4c1.105,0,2-.895,2-2s-.895-2-2-2-2,.895-2,2,.895,2,2,2Zm4,3c1.105,0,2-.895,2-2s-.895-2-2-2-2,.895-2,2,.895,2,2,2Zm4-3c1.105,0,2-.895,2-2s-.895-2-2-2-2,.895-2,2,.895,2,2,2Z"/>
                  </svg>
                </label>
                <input type="radio" v-model="withWho" name="withWho" value="Couple" id="Couple"/>
                <label for="Couple" :class="{ selected: withWho === 'Couple' }">
                  <svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24">
                    <path d="m7.752,17.084c.364.415.323,1.047-.093,1.411-.414.364-1.046.323-1.411-.093l-2.043-2.33c-.083-.095-.23-.125-.308-.063-1.138.893-1.897,1.913-1.897,3.991v3c0,.552-.448,1-1,1s-1-.448-1-1v-3c0-3.082,1.423-4.593,2.664-5.565.92-.72,2.256-.579,3.045.319l2.043,2.331Zm-3.613-10.093h0c.014,0,.027,0,0,0Zm17.168,7.421c-.926-.719-2.264-.568-3.047.34l-1.266,1.468-1.285-1.466c-.789-.898-2.125-1.039-3.045-.319-1.24.972-2.664,2.483-2.664,5.565v3c0,.552.448,1,1,1s1-.448,1-1v-3c0-2.078.759-3.098,1.897-3.991.078-.061.224-.031.308.063l2.043,2.33c.19.217.464.341.752.341h.004c.29,0,.564-.127.753-.347l2.017-2.338c.082-.095.228-.128.308-.066.997.773,1.918,1.793,1.918,4.007v3c0,.552.448,1,1,1s1-.448,1-1v-3c0-3.102-1.439-4.615-2.693-5.587Zm-11.327-3.711c.11.541-.24,1.069-.782,1.178-.393.08-.796.12-1.198.12-2.17,0-4.069-1.162-5.123-2.892-.309,1.397-.64,2.907-.9,4.104-.102.468-.516.788-.976.788-.07,0-.142-.007-.213-.023-.54-.117-.882-.65-.765-1.189.282-1.299,1.701-7.807,1.876-8.351C2.758,1.783,5.209,0,8,0c1.75,0,3.391.718,4.587,1.949,1.097-1.194,2.667-1.949,4.413-1.949,3.309,0,6,2.691,6,6s-2.691,6-6,6-6-2.691-6-6c0-.818.166-1.597.463-2.308-.273-.347-.587-.652-.941-.899-.528,1.312-1.447,2.424-2.67,3.187-1.081.674-2.469,1.011-3.713,1.011-.028,0-.014,0,0,0,.444,1.724,1.999,3.008,3.86,3.008.269,0,.539-.027.802-.08.539-.111,1.069.24,1.178.782Zm3.02-4.702c0,2.206,1.794,4,4,4s4-1.794,4-4-1.794-4-4-4-4,1.794-4,4Zm-9.158-1.042c1.031.102,2.059-.118,2.952-.675.855-.533,1.491-1.313,1.862-2.228-.216-.032-.434-.054-.656-.054-1.886,0-3.54,1.187-4.158,2.958Z"/>
                  </svg>
                </label>
                <input type="radio" v-model="withWho" name="withWho" value="Kids Family" id="Kids Family"/>
                <label for="Kids Family" :class="{ selected: withWho === 'Kids Family' }">
                  <svg xmlns="http://www.w3.org/2000/svg" width="100px" height="100px" id="Layer_1" data-name="Layer 1" viewBox="0 0 24 24"><path d="M24,11.5a3.5,3.5,0,0,0-2.149-3.226,10,10,0,0,0-19.7,0,3.5,3.5,0,0,0,1.119,6.718,10.607,10.607,0,0,0,2.071,2.955,8.908,8.908,0,0,0-2.272,4.928,1,1,0,0,0,.868,1.117A1.093,1.093,0,0,0,4.061,24a1,1,0,0,0,.991-.875,6.924,6.924,0,0,1,1.815-3.872A8.948,8.948,0,0,0,12,21a8.94,8.94,0,0,0,5.119-1.74,6.922,6.922,0,0,1,1.808,3.862,1,1,0,0,0,.991.876,1.063,1.063,0,0,0,.125-.008,1,1,0,0,0,.868-1.116,8.9,8.9,0,0,0-2.261-4.918,10.622,10.622,0,0,0,2.082-2.966A3.5,3.5,0,0,0,24,11.5Zm-3.752,1.473a.993.993,0,0,0-1.117.651C18.215,16.222,15.13,19,12,19s-6.215-2.78-7.131-5.378a.994.994,0,0,0-1.117-.651A1.606,1.606,0,0,1,3.5,13a1.5,1.5,0,0,1-.27-2.972,1,1,0,0,0,.816-.878A7.961,7.961,0,0,1,8.13,3a4.075,4.075,0,0,0-.022,1.942,4,4,0,0,0,7.688.318A.977.977,0,0,0,14.851,4H14.7a.867.867,0,0,0-.806.631A2,2,0,1,1,12,2a7.978,7.978,0,0,1,7.954,7.15,1,1,0,0,0,.816.878A1.5,1.5,0,0,1,20.5,13,1.606,1.606,0,0,1,20.248,12.973Z"/><circle cx="9.5" cy="11.5" r="1.5"/><circle cx="14.5" cy="11.5" r="1.5"/></svg>
                </label>
              </div>
            </div>
          </div>
          <div class="arrow-container">
            <img src="@/assets/images/whitearrow.gif" width="100px" height="50px">
          </div>
        </div>
        <button type="submit" value="제출" class="buttonSubmit">
          <svg width="30" height="30" viewBox="0 0 30 30" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <rect width="30" height="30" fill="url(#pattern0_187_2)"/>
          <defs>
          <pattern id="pattern0_187_2" patternContentUnits="objectBoundingBox" width="1" height="1">
          <use xlink:href="#image0_187_2" transform="scale(0.0333333)"/>
          </pattern>
          <image id="image0_187_2" width="30" height="30" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAACXBIWXMAAAsTAAALEwEAmpwYAAABz0lEQVR4nO2Wu0pDQRCGvYAWopIUFt6w1s5SOx8gKMHaPmosfBpRfAB7L7WFRgQVvEXt9A28FErkk4U/sITsnN2YgIU/HMLJmZ3vzOzM7Onq+tdfEzAJrANHQBV411XVf2vARDuBY8AWUCNb38AeMPVb6CLwFoDMAfOBZ69AoVXohiJoKs/Oir7cSqTfVk4jwHV4XOTAuJHeVHA97aMx4N0IZylgp+2Ylql1AFxzmbTA5UhHqWCnVQt8SOfA+xb4qYPgqgV2FehrLmicDn5NAc8ngq81eGaAASAHzAKbwK3l5IHW9AmUgB7Dd3dbiqsBuqD1/eqMind6VXRy9VlgZ5CqkneKXRl2l84mBJ6IHSDenvYq0jr0GSgCg7qWdGY7XQQjB3YSwBsNg8dB80185oEXc5AoZY3VHdK01pzpvmhs47JsTq29LmQdi9Kg7N/8+4DPocx+9tKXBc8lgIdl826CvcittM/KzrWM05LhqyibSiZYC0bdeRqo9k3ZuK9PVL2h4nqUzUoUuOHLZBU4AO6V3js3kdROrk9R9S5rT4cU6aOefUV9jSS+2JgHb6Yv/breH2k3vE/T70QZ+dD+r2jLbgQ/bys44sVGHBQ4/gFrjgYFC8HUNgAAAABJRU5ErkJggg=="/>
          </defs>
          </svg>
          <p style="color: white; font-size: 15px;"><strong>시추</strong> 받기</p>
        </button>
      </form>
    </div>
    <div class="main-container-big _2" ref="bottomDiv">
			<AITextModal
				:isModalOpen="isModalOpen"
				:AIText="AIText"
        :prompt="prompt"
				@closeModal="closeModal"
			/>
      <RecommendMovie :movies="shihtzuRecommendMovies"/>
    </div>
  </main>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { useAuthStore } from '@/stores/auth';
import RecommendMovie from '@/components/RecommendMovie.vue'
import AITextModal from '@/components/AITextModal.vue'

const store = useMovieStore()
const authstore = useAuthStore()

const preferences = store.preferences
const AIToggle = ref(false);
const bottomDiv = ref(null);
const isModalOpen = ref(false);
const AIText = ref('');
const prompt = ref('');

const where = ref('Theater');
const withWho = ref('Alone');

const shihtzuRecommendMovies = ref()

// 스크롤 비활성화 함수
const disableScroll = () => {
  document.body.style.overflow = 'hidden';
};

// 스크롤 활성화 함수
const enableScroll = () => {
  document.body.style.overflow = '';
};

const submitForm = async () => {
  if (store.selectedOption === 'now') {
    preferences.time = 'now';
  } else if (store.selectedOption === 'left') {
    preferences.time = '13:00';
  } else if (store.selectedOption === 'right') {
    preferences.time = '21:00';
  }
  preferences.where = where.value;
	preferences.withWho = withWho.value;
	preferences.isWeekend = store.selectedOption === 'right';
	if (AIToggle.value) {
    prompt.value = `다음 조건으로 영화 장르 추천해줘! : ${where.value}, ${withWho.value}, ${preferences.time}`
		openModal()
		await store.AIRecommend(preferences)
		shihtzuRecommendMovies.value = store.shihtzuRecommendMovies
		AIText.value = store.AIText
	} else {
		await store.shihtzuMovies(preferences)
		shihtzuRecommendMovies.value = store.shihtzuRecommendMovies
	}

	bottomDiv.value.scrollIntoView({ behavior: 'smooth' });
};

const openModal = () => {
  isModalOpen.value = true;
};

const closeModal = () => {
  isModalOpen.value = false;
  prompt.value = ''
  AIText.value = ''
};

// 페이지 로드 시 스크롤 비활성화
onMounted(() => {
  disableScroll();
});

// 페이지를 벗어날 때 스크롤 활성화
onBeforeUnmount(() => {
  enableScroll();
});


</script>

<style scoped>
.about-gpt {
  color: white;
  margin-left: 10px;
}
.main-container {
	height: 46vh;
}
.main-container-big {
	height: 92vh;
}
._1 {
	background-color: #222831;	
}
._2 {
	background-color: #393e46;
}
.searchForm {
	display: flex;
	flex-direction: column;
	align-items: center;
	width: 100%;
	height: 100%;
}
.buttonSubmit {
	margin-top: 20px;
	font-size: 30px;
	cursor: pointer;
	background-color: #393E46;
	border: none;
	transition: transform 0.3s ease-in-out;
}
.buttonSubmit:hover {
  transform: scale(1.15);
}
.form-inner {
	width: 100%;
	height: 85%;
	background-color: #1b1b1b;
	border-bottom-left-radius: 40px;
	border-bottom-right-radius: 40px;
	display: flex;
	flex-direction: column;
	align-items: center;
}
.input-container {
	background-color: #1b1b1b;
	width: 90%;
	height: 80%;
	display: flex;
	flex-direction: column;
	justify-content: space-around;
}
label svg {
  fill: #393E46; /* 기본 색상 */
  transition: fill 0.3s ease-in-out;
	cursor: pointer;
}

label.selected svg {
  fill: #0092ca; /* 선택된 색상 */
	transform: scale(1.2);
}
.shihtzu-tinytitle {
	width: 600px;
	color: #eeeeee;
	font-size: 30px;
}
.input-innercont {
	width: 100%;
	display: flex;
	flex-direction: row;
	align-items: center;
}
.shihtzu-select {
	width: 70%;
	display: flex;
	flex-direction: row;
	justify-content: space-around;
}
.shihtzu-select > input {
	display: none;
}
.arrow-container {
	margin-top: 100px;
}
.input-titlecont {
	display: flex;
	flex-direction: row;
	align-items: center;
}
.time-selectbox {
	background-color: #1b1b1b;
	border: 1px solid gray;
	color: #eeeeee;
	border-radius: 10px;
	width: 200px;
	height: 50px;
	padding-left: 10px;
	font-size: 15px;
  margin-right: 40px;
}
.where-who {
	margin-left: 100px;
}
.where-who > strong {
	margin-left: 50px;
}
/* 버튼 시도하기 */
.switch {
  position: relative;
  margin-left: 20px;
}
.switch input {
  height: 100%;
  width: 100%;
  position: absolute;
  left: 0;
  top: 0;
  opacity: 0;
  z-index: 100;
  cursor: pointer;
}
.switch label {
  height: 55px; /* 기존 110px에서 줄임 */
  width: 110px; /* 기존 220px에서 줄임 */
  background-color: #393E46; /* 변경된 배경색 */
  border-radius: 100px;
  display: block;
  box-shadow: inset 0 0 20px rgba(0,0,0,0.2), inset 0 0 5px -2px rgba(0,0,0,0.4);
}
.switch label .bulb {
  height: 45px; /* 기존 90px에서 줄임 */
  width: 45px; /* 기존 90px에서 줄임 */
  background-color: #393E46; /* 변경된 배경색 */
  border-radius: 50%;
  position: relative;
  top: 5px; /* 기존 10px에서 줄임 */
  left: 5px; /* 기존 10px에서 줄임 */
  display: block;
  transition: 0.7s;
  box-shadow: inset 0 0 1px 3px #393E46, inset 0 0 6px 8px #423963, 0 20px 30px -10px rgba(0,0,0,0.4);
}
.switch label .bulb .bulb-center {
  position: absolute;
  display: block;
  height: 18px; /* 기존 36px에서 줄임 */
  width: 18px; /* 기존 36px에서 줄임 */
  background-color: #5a527b;
  border-radius: 50%;
  top: 50%;
  left: 50%;
  transition: 0.7s;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  box-shadow: inset 0 0 0 4px #635a84;
}
.switch label .bulb .bulb-center:after {
  content: "";
  display: block;
  height: 7px; /* 기존 14px에서 줄임 */
  width: 7px; /* 기존 14px에서 줄임 */
  background-color: #7b7394;
  border-radius: 50%;
  position: absolute;
  transition: 0.7s;
  top: 50%;
  left: 50%;
  -webkit-transform: translate(-50%, -50%);
          transform: translate(-50%, -50%);
  box-shadow: 0 0 2px 4px #524a73;
}
.switch label .bulb .filament-1,
.switch label .bulb .filament-2 {
  position: absolute;
  display: block;
  height: 17.5px; /* 기존 35px에서 줄임 */
  width: 17.5px; /* 기존 35px에서 줄임 */
  border-radius: 50%;
  top: 50%;
  left: 50%;
  overflow: hidden;
  -webkit-transform: translate(-50%, -50%) rotate(-45deg);
          transform: translate(-50%, -50%) rotate(-45deg);
}
.switch label .bulb .filament-1:after,
.switch label .bulb .filament-2:after,
.switch label .bulb .filament-1:before,
.switch label .bulb .filament-2:before {
  content: "";
  display: block;
  height: 3px; /* 기존 6px에서 줄임 */
  width: 8.5px; /* 기존 17px에서 줄임 */
  border-radius: 50%;
  border: 2px solid #4a426b;
  position: absolute;
  transition: 0.7s;
  top: -2px; /* 기존 -4px에서 줄임 */
  left: -1px; /* 기존 -2px에서 줄임 */
  -webkit-transform: rotate(-10deg);
          transform: rotate(-10deg);
}
.switch label .bulb .filament-1:before,
.switch label .bulb .filament-2:before {
  left: 7.5px; /* 기존 15px에서 줄임 */
  -webkit-transform: rotate(10deg);
          transform: rotate(10deg);
}
.switch label .bulb .filament-2 {
  -webkit-transform: translate(-50%, -50%) rotate(45deg) !important;
          transform: translate(-50%, -50%) rotate(45deg) !important;
}
.reflections {
  height: 100%;
  width: 100%;
  display: block;
  border-radius: 50%;
  overflow: hidden;
  position: absolute;
  z-index: 90;
  -webkit-perspective: 70px;
          perspective: 70px;
}
.reflections span {
  height: 40px; /* 기존 80px에서 줄임 */
  width: 40px; /* 기존 80px에서 줄임 */
  border-radius: 50%;
  background-image: linear-gradient(-135deg, transparent 10%, rgba(255,255,255,0.3));
  position: absolute;
  left: -20px; /* 기존 -40px에서 줄임 */
  bottom: -22.5px; /* 기존 -45px에서 줄임 */
}
.reflections span:after {
  content: "";
  display: block;
  height: 7px; /* 기존 14px에서 줄임 */
  width: 10px; /* 기존 20px에서 줄임 */
  position: absolute;
  top: -18px; /* 기존 -36px에서 줄임 */
  right: -20px; /* 기존 -40px에서 줄임 */
  border-radius: 50%;
  box-shadow: 4px -2px 0 -3px rgba(255,255,255,0.4);
  -webkit-filter: blur(1px);
          filter: blur(1px);
  -webkit-transform: rotate(-10deg);
          transform: rotate(-10deg);
}
.reflections:after {
  content: "";
  display: block;
  height: 40px; /* 기존 80px에서 줄임 */
  width: 25px; /* 기존 50px에서 줄임 */
  background-image: linear-gradient(80deg, rgba(255,255,255,0.05) 45%, rgba(255,255,255,0.5));
  border-radius: 10% 20% 50% 30%/30% 60% 30% 40%;
  position: absolute;
  -webkit-transform-style: preserve-3d;
          transform-style: preserve-3d;
  -webkit-transform: rotateX(-25deg) rotate(-35deg) skewx(-15deg) translate(10px, -20px);
          transform: rotateX(-25deg) rotate(-35deg) skewx(-15deg) translate(10px, -20px);
  top: -8px;
  left: -5px;
}
.reflections:before {
  content: "";
  display: block;
  position: absolute;
  height: 5px; /* 기존 10px에서 줄임 */
  width: 15px; /* 기존 30px에서 줄임 */
  background-image: linear-gradient(to right, transparent, rgba(255,255,255,0.15));
  bottom: 5px; /* 기존 10px에서 줄임 */
  right: 0px;
  -webkit-transform: rotate(45deg);
          transform: rotate(45deg);
}
.sparks .spark1 {
  display: block;
  height: 0.5px; /* 기존 1px에서 줄임 */
  width: 0.5px; /* 기존 1px에서 줄임 */
  background-color: #d1b82b;
  position: absolute;
  right: -2.5px; /* 기존 -5px에서 줄임 */
  border-radius: 50%;
  bottom: 11.5px; /* 기존 23px에서 줄임 */
  transition: 0.4s;
  opacity: 0;
}
.sparks .spark2 {
  display: block;
  height: 1.5px; /* 기존 3px에서 줄임 */
  width: 1.5px; /* 기존 3px에서 줄임 */
  background-color: #d1b82b;
  position: absolute;
  right: 10px; /* 기존 20px에서 줄임 */
  border-radius: 50%;
  bottom: 40px; /* 기존 80px에서 줄임 */
  transition: 0.4s;
  opacity: 0;
}
.sparks .spark3 {
  display: block;
  height: 1.5px; /* 기존 3px에서 줄임 */
  width: 1.5px; /* 기존 3px에서 줄임 */
  background-color: #d1b82b;
  position: absolute;
  left: 10px; /* 기존 20px에서 줄임 */
  border-radius: 50%;
  bottom: 40px; /* 기존 80px에서 줄임 */
  transition: 0.4s;
  opacity: 0;
}
.sparks .spark4 {
  display: block;
  height: 1.5px; /* 기존 3px에서 줄임 */
  width: 1.5px; /* 기존 3px에서 줄임 */
  background-color: #d1b82b;
  position: absolute;
  left: 10px; /* 기존 20px에서 줄임 */
  border-radius: 50%;
  bottom: 10px; /* 기존 20px에서 줄임 */
  transition: 0.4s;
  opacity: 0;
}
.switch input:checked ~ label .bulb {
  left: 60px; /* 기존 120px에서 줄임 */
  background-color: #a7694a;
  box-shadow: inset 0 0 1px 3px #a56758, inset 0 0 6px 8px #6b454f, 0 20px 30px -10px rgba(0,0,0,0.4), 0 0 30px 50px rgba(253,184,67,0.1);
}
.switch input:checked ~ label .bulb > .bulb-center {
  background-color: #feed6b;
  box-shadow: inset 0 0 0 4px #fdec6a, 0 0 12px 10px #bca83c, 0 0 20px 14px #a1664a;
}
.switch input:checked ~ label .bulb > .bulb-center:after {
  background-color: #fef401;
  box-shadow: 0 0 2px 4px #fdb843;
}
.switch input:checked ~ label .bulb >.filament-1:before,
.switch input:checked ~ label .bulb >.filament-2:before,
.switch input:checked ~ label .bulb >.filament-1:after,
.switch input:checked ~ label .bulb >.filament-2:after {
  border-color: #fef4d5;
}
.switch input:checked ~ label .bulb > .sparks .spark1 {
  height: 0.5px; /* 기존 1px에서 줄임 */
  width: 0.5px; /* 기존 1px에서 줄임 */
  -webkit-animation: spark1 2s ease-in-out;
          animation: spark1 2s ease-in-out;
  -webkit-animation-delay: 0.4s;
          animation-delay: 0.4s;
}
.switch input:checked ~ label .bulb > .sparks .spark2 {
  height: 1.5px; /* 기존 3px에서 줄임 */
  width: 1.5px; /* 기존 3px에서 줄임 */
  -webkit-animation: spark2 2.4s ease-in-out;
          animation: spark2 2.4s ease-in-out;
  -webkit-animation-delay: 0.4s;
          animation-delay: 0.4s;
}
.switch input:checked ~ label .bulb > .sparks .spark3 {
  height: 1px; /* 기존 1.5px에서 줄임 */
  width: 1px; /* 기존 1.5px에서 줄임 */
  -webkit-animation: spark3 2s ease-in-out;
          animation: spark3 2s ease-in-out;
  -webkit-animation-delay: 0.9s;
          animation-delay: 0.9s;
}
.switch input:checked ~ label .bulb > .sparks .spark4 {
  height: 1px; /* 기존 1.5px에서 줄임 */
  width: 1px; /* 기존 1.5px에서 줄임 */
  -webkit-animation: spark4 1.7s ease-in-out;
          animation: spark4 1.7s ease-in-out;
  -webkit-animation-delay: 0.9s;
          animation-delay: 0.9s;
}
@-webkit-keyframes spark1 {
  0% {
    right: -2.5px; /* 기존 -5px에서 줄임 */
    height: 0.5px; /* 기존 1px에서 줄임 */
    width: 0.5px; /* 기존 1px에서 줄임 */
    opacity: 0;
  }
  20% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
    right: 0px;
    opacity: 1;
  }
  30% {
    right: -2.5px; /* 기존 -5px에서 줄임 */
    opacity: 1;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
  70% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
  100% {
    right: -30px; /* 기존 -60px에서 줄임 */
    bottom: 20px; /* 기존 40px에서 줄임 */
    opacity: 0;
  }
}
@keyframes spark1 {
  0% {
    right: -2.5px; /* 기존 -5px에서 줄임 */
    height: 0.5px; /* 기존 1px에서 줄임 */
    width: 0.5px; /* 기존 1px에서 줄임 */
    opacity: 0;
  }
  20% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
    right: 0px;
    opacity: 1;
  }
  30% {
    right: -2.5px; /* 기존 -5px에서 줄임 */
    opacity: 1;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
  70% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
  100% {
    right: -30px; /* 기존 -60px에서 줄임 */
    bottom: 20px; /* 기존 40px에서 줄임 */
    opacity: 0;
  }
}
@-webkit-keyframes spark2 {
  0% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
    opacity: 0;
  }
  30% {
    opacity: 1;
  }
  100% {
    right: -10px; /* 기존 -20px에서 줄임 */
    bottom: 50px; /* 기존 100px에서 줄임 */
    opacity: 0;
  }
}
@keyframes spark2 {
  0% {
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
    opacity: 0;
  }
  30% {
    opacity: 1;
  }
  100% {
    right: -10px; /* 기존 -20px에서 줄임 */
    bottom: 50px; /* 기존 100px에서 줄임 */
    opacity: 0;
  }
}
@-webkit-keyframes spark3 {
  0% {
    opacity: 0;
  }
  30% {
    opacity: 1;
    height: 1px; /* 기존 2px에서 줄임 */
    width: 1px; /* 기존 2px에서 줄임 */
  }
  100% {
    left: 0px;
    bottom: 50px; /* 기존 100px에서 줄임 */
    opacity: 0;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
}
@keyframes spark3 {
  0% {
    opacity: 0;
  }
  30% {
    opacity: 1;
    height: 1px; /* 기존 2px에서 줄임 */
    width: 1px; /* 기존 2px에서 줄임 */
  }
  100% {
    left: 0px;
    bottom: 50px; /* 기존 100px에서 줄임 */
    opacity: 0;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
}
@-webkit-keyframes spark4 {
  0% {
    opacity: 0;
  }
  30% {
    opacity: 1;
    height: 1px; /* 기존 2px에서 줄임 */
    width: 1px; /* 기존 2px에서 줄임 */
  }
  100% {
    left: -10px; /* 기존 -20px에서 줄임 */
    bottom: -5px; /* 기존 -10px에서 줄임 */
    opacity: 0;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
}
@keyframes spark4 {
  0% {
    opacity: 0;
  }
  30% {
    opacity: 1;
    height: 1px; /* 기존 2px에서 줄임 */
    width: 1px; /* 기존 2px에서 줄임 */
  }
  100% {
    left: -10px; /* 기존 -20px에서 줄임 */
    bottom: -5px; /* 기존 -10px에서 줄임 */
    opacity: 0;
    height: 1.5px; /* 기존 3px에서 줄임 */
    width: 1.5px; /* 기존 3px에서 줄임 */
  }
}


</style>
