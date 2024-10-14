<template>
  <div class="containertoRecommend">
    <div class="toRecommend-title">
      <p><strong>|</strong> Recommend For <strong>You</strong></p>
    </div>
    <div class="toRecommend-container">
      <div class="leftside-container" @mouseover="expandLeft" @mouseleave="shrinkLeft" @click="navigateToShihTzuView">
        <svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="90" height="90" fill="url(#pattern0_168_2)"/>
        <defs>
        <pattern id="pattern0_168_2" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_168_2" transform="scale(0.0111111)"/>
        </pattern>
        <image id="image0_168_2" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAAFi0lEQVR4nO2dW4scRRTHz3pNFPVZCCRzziyBgMmc6rjGQLLeHswHUBFZ/AQqURQVwcurkosb2TXfwVvWTeKLCIriS4yJF/AlMCDJ1JndCCFiTNiR07OEvcxM96zd1dU99YeCYXenu+q3p09VnTpVDRAUFFSgOgC3hH9Ajmru2bLZMh6zTH/FxeC0/ixAz1jCdEQMdVYXPBRAZw/60nrQ1AqgswZt1kGOSwAdQJdTEiw6gK6UJFh0AF0pSbDoADp3yd7t99gIX9QZmjX0dAdgrCoW3QEYs0zP6IzUGnxJ2wpF6OLOnXdbpvMrG20Nfv5HvX5nHvezhi6vhWwNLeZxL22DNfjFqvsxndM2g2u1mF7oY2Un84BtGY/1iHV8mPV9tO7ahl5t0zaDa2kj+z3OecBuavTO0KwwXdViDc1kHb0bBHnZqo+Aa4mpPTcAdG6W3QEYy6MvSISsrqqBz0IRAXhr8EQRsAuBbPBEYYsOnR077kiEzXj6wuTWTeCpStOGNNYghk52ouh28ExapzR19+apTPfo0ZvgmSzjW6WBnBa2ZfwBPJNl+rFUkFPBZjw99LUielSY3rOMn1mDv+kExTL+aw1eiz8b/FV/J0zvSkSPDAtG61Q6yINgW0NLLaYn03xfDEXCeFxXuhMe617uSWePH9uITJp72QYe0LqVDvLKTkZ9sjX4vVpNKwVkhWMZvxoWbv+Cp1q7xhuJ923gAa2j1rVt6A0fO+1M1NyzZbMwHbVMN7KDfLNfuC5MhwsfmhUt2b1tuwZrsgbco5y1DRyHUZQ0ag+KQesA8rJ100KrQXthlNSOxh8Sg1dcQV7ht6+0o9oEjIq7sIxt95CXC6NU3o1cmNy6SQz+VBjkm7DpXKUTJIXpaOGQq54gaeNxcvZDuI0WrUuacXbpZDOdjGTmQuahShKdVhcNtZdVG1qyu+sMVZEwHi8a6gDYM1AFxUv3PHyAyCHoRV1lgbJLDD5WNMxE2Dy+H8oujSeLBzAHFqZ3oOxal/Fj/CuW6VOnUP6M7r/LMn6U1qdqoF0ziAbNsnRlRDyAObgd+ItLJprfNruxitJs32sWGdcwKQujOGOiySHC9PfGKkpX+yWX6PqeFA0yseA/zpgE0OCMyf95TPoO+kfYdcwkZGzidK9c5D4XW9Ss0ip3hs0cmOQiTU4XD2AmwPkEyq44ucV4b9FvQ9kVZxsZ30HX9kHZ1d0PQpe9hcy0UImgkkpCmNTdMpZ46TJoqXLLWWLwVNFg1xWmOaiaLkX4QJwL541vxuutxrZdUEUJ02GPQL8PlU6gYTxTNGQx9HOlE2hUmo6lsYXiIKNtRXWCUVA7qk0UleSoWawwSpIC0nYXmB6GUZRVN2LobO6gGc+MjLtIyDA9lMfQT69pGT+o7NaKzuTkbWLwVTH4jU4KhPHxpO/omFZz4XrskhoesF6DaU7H7kn31brp31rGryWiV7TuUAbF29+Y5tf4xxtpYKs0F05XNboB9OH9sK5spJ1Wtxu1J9ZluDLNe7/9bfCGTpobejM8j+/X5BbNu9BVEF0W627mxGvxZ6bzGrSP/8bU9g0bhROmL/v80/zda5jiUJFvwTMJ03cDnhD/YKc64YDxNfBMEuHrCe7IH9ipj5GY9K+T6XbaJThGojSHipS5DZ2n4NZ46Oa7NWTm+mhO2wyu1Y7w+SIgd3I61ygl7ClwLc2wdAm56eBlComHuxicBteyTC+7tGRx9DKFQbC1zeBaixHeZ5l+X+vH8vLJ0utlCkwXc5zdrup/NLWtPVG/F4pQF3b9YHycJdNUnufCSZ/HOefOfqrrruoHC4PsWuIY9MhKAugAulKSYNEBdKUkwaID6EpJgkW7kXX4MoWRlnX0MoWRV9PByxSCHLxMISgoCIbQf8GW/4qh8N1TAAAAAElFTkSuQmCC"/>
        </defs>
        </svg>
        <p class="black-font">집중 잘되는 <strong>주말 오후!</strong></p>
      </div>
      <div class="linkToRecommendButton" @click="navigateToShihTzuView">
        <svg viewBox="0 0 100 100" width="100" height="100" class="clock">
          <circle cx="50" cy="50" r="45" stroke="white" stroke-width="3" fill="none" />
          <line x1="50" y1="50" x2="50" y2="20" stroke="white" stroke-width="2" id="hour-hand" />
          <line x1="50" y1="50" x2="50" y2="10" stroke="white" stroke-width="2" id="minute-hand" />
          <line x1="50" y1="50" x2="50" y2="5" stroke="red" stroke-width="1" id="second-hand" />
        </svg>
        <p class="button-link-title">현재 <strong>시</strong>간으로 <strong>추</strong>천</p>
      </div>
      <div class="rightside-container" @mouseover="expandRight" @mouseleave="shrinkRight" @click="navigateToShihTzuView">
        <svg width="90" height="90" viewBox="0 0 90 90" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <rect width="90" height="90" fill="url(#pattern0_141_6)"/>
        <defs>
        <pattern id="pattern0_141_6" patternContentUnits="objectBoundingBox" width="1" height="1">
        <use xlink:href="#image0_141_6" transform="scale(0.0111111)"/>
        </pattern>
        <image id="image0_141_6" width="90" height="90" xlink:href="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAFoAAABaCAYAAAA4qEECAAAACXBIWXMAAAsTAAALEwEAmpwYAAADuElEQVR4nO2cWahNURiAPy4is0KJTGV6MJaIkESeJBEPpsKjIlG6yoOhLg94NYuUIVOSRJnKEA9kzFBKyBDdcK/p18oS9zjnOOfsYa299//V/3zW+s7Z6/x7/f9aoCiKoiiKoiiKoihKimkGzARWAmNdDyaNNAUWAE8B+SvWuB5YmhgP3M0R/Du+A71cDzDptAf2FhD8d0xxPdAkMw54VoJkE/1cDzapLAK+lij5vOvBJpEmwLYSBYsuG5WnbYfKlPwQaBzyl516yafKlCzActcDTxKNgN0VSBagr+vBJ4maCiXfdz3wJDED+FGh6I2uB58UzGNfW6FkAWa5nkASMJnCxQCSBRjgehJJYFlAyZ9tzq0UoUvAJUNs/qz8h10BJQtwTS0Xp5/d1gwq+oyKLk6lLyaSE4dVdGG6Al9CEn1cRRdmVUiSBTinogvnzU9CFH1dRednRIiSBXilovOzNmTRAnRQ2f9yMwLRI1V0Q9oA3yIQvVRFN2RSBJIFOKGiG7IiItEfbPeSYim3ql1OTFHLfzgfoehDKvoPDyIUXQd0Utm/eBOhaAHWqehflNraFeRPsb3KjiaHlpzYoKLD2xqVImGemkFZlx20PiglhqmqV5FhHsUkWoDVZJhLMYr+Zo9hZJJyW3GDxvusrtfrYxYtwHOgBxljugPRYo/J9SFD9HYkWmzJaxgZajR/7VD2R2A+GWGPQ9Fiw4yhLSnH1TotOfECmGOfstTWDes9EC02LtkSWxy0BKYC8+LKhPZ7IFjydKXOtjLCpj+wxeb1vz+v3j5RkTLWA7FSIGptA6Y5U9OxwvmZ5WgoUA1cKXI252Mc27p3PJAq/wkj6Bawz/YLmrMyE4Dh9jjHEHtO3dQrFwKbgbNlZlajoxY91wOR4jjMlm7nqEVXJeRXLRHGVmJimgeTFUfxCegWl2jzp3Hag0mLgzD3QMVK9xgrL+JJ3HbVWbXYg8lLTFFnUz8nmCXkiAcSJIZYgmNaZSALOejL3oo5e/jWAyES0St+CzxiMPDOAzESYjyI48WkEkalKBO5Z8+8e4vZT3jpgSgJEDcCbEzFSs8i12OK53EUaE2CaAcc8ECclNG4szrJV8PNScC6/Swt1yv3Ao55IDTfducmW6ZLFRM9erk5CQwkxTS226xXHcj9bq+viLw64htjgJ05xc+o+vhqstZelo/m9le+A3gcUs3wjr3AcHzWm9uL0c1Ws6ttd9Jl2wz/MieDeWvf4C4A2+0J38l6a4KiKIqiKIqiKAql8xNSKRqpmfcoiwAAAABJRU5ErkJggg=="/>
        </defs>
        </svg>
        <p class="black-font">가벼운 마무리 <strong>평일 저녁</strong></p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import { useRouter } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const router = useRouter();
const store = useMovieStore();

// const expandLeft = () => {
//   const leftContainer = document.querySelector('.leftside-container');
//   const rightContainer = document.querySelector('.rightside-container');
//   leftContainer.style.width = '40%';
//   rightContainer.style.width = '20%';
//   leftContainer.style.backgroundColor = 'white';
// };

// const shrinkLeft = () => {
//   const leftContainer = document.querySelector('.leftside-container');
//   const rightContainer = document.querySelector('.rightside-container');
//   leftContainer.style.width = '30%';
//   rightContainer.style.width = '30%';
//   leftContainer.style.backgroundColor = 'white';
// };

// const expandRight = () => {
//   const leftContainer = document.querySelector('.leftside-container');
//   const rightContainer = document.querySelector('.rightside-container');
//   leftContainer.style.width = '20%';
//   rightContainer.style.width = '40%';
//   rightContainer.style.backgroundColor = 'white';
// };

// const shrinkRight = () => {
//   const leftContainer = document.querySelector('.leftside-container');
//   const rightContainer = document.querySelector('.rightside-container');
//   leftContainer.style.width = '30%';
//   rightContainer.style.width = '30%';
//   rightContainer.style.backgroundColor = 'white';
// };

const expandLeft = () => {
  const leftContainer = document.querySelector('.leftside-container');
  const rightContainer = document.querySelector('.rightside-container');
  leftContainer.style.width = '40%';
  rightContainer.style.width = '20%';
  leftContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  leftContainer.style.backgroundColor = 'rgb(255, 172, 168)';
};

const shrinkLeft = () => {
  const leftContainer = document.querySelector('.leftside-container');
  const rightContainer = document.querySelector('.rightside-container');
  leftContainer.style.width = '30%';
  rightContainer.style.width = '30%';
  leftContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  leftContainer.style.backgroundColor = 'white';
};

const expandRight = () => {
  const leftContainer = document.querySelector('.leftside-container');
  const rightContainer = document.querySelector('.rightside-container');
  leftContainer.style.width = '20%';
  rightContainer.style.width = '40%';
  leftContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.backgroundColor = 'rgb(217, 170, 255)';
};

const shrinkRight = () => {
  const leftContainer = document.querySelector('.leftside-container');
  const rightContainer = document.querySelector('.rightside-container');
  leftContainer.style.width = '30%';
  rightContainer.style.width = '30%';
  leftContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.transition = 'width 0.6s ease, background-color 0.6s ease';
  rightContainer.style.backgroundColor = 'white';
};

const navigateToShihTzuView = (event) => {
  if (event.target.classList[0] === 'leftside-container') {
    store.selectedOption = 'left'
    store.submitPreferences('13:00', '', '', true);
  } else if (event.target.classList[0] === 'rightside-container') {
    store.selectedOption = 'right'
    store.submitPreferences('20:00', '', '', false);
  } else {
    store.selectedOption = 'now'
    store.submitPreferences('now', '', '', false);
  }
  router.push('/shihtzu');
};

const updateClock = () => {
  const now = new Date();
  const second = now.getSeconds();
  const minute = now.getMinutes();
  const hour = now.getHours();

  const secondHand = document.getElementById('second-hand');
  const minuteHand = document.getElementById('minute-hand');
  const hourHand = document.getElementById('hour-hand');

  if (secondHand && minuteHand && hourHand) {
    secondHand.setAttribute('transform', `rotate(${second * 6}, 50, 50)`);
    minuteHand.setAttribute('transform', `rotate(${minute * 6}, 50, 50)`);
    hourHand.setAttribute('transform', `rotate(${(hour % 12) * 30 + minute / 2}, 50, 50)`);
  }
};

let clockInterval;

onMounted(() => {
  updateClock();
  clockInterval = setInterval(updateClock, 1000);
});

onBeforeUnmount(() => {
  clearInterval(clockInterval);
});
</script>


<style scoped>
* {
  color: white;
}
.containertoRecommend {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.toRecommend-title {
  align-self: flex-start;
  margin-left: 40px;
  margin-top: 40px;
  font-weight: bold;
  font-size: 20px;
}
.toRecommend-container {
  margin-top: 40px;
  width: 100%;
  height: 30vh;
  display: flex;
  justify-content: space-between;
  flex-direction: row;
}
.toRecommend-container > div {
  width: 30%;
  transition: width 0.5s ease;
}
.leftside-container {
  border-top-right-radius: 100px;
  border-bottom-right-radius: 100px;
  background-color: #eeeeee;
  padding-left: 30px;
  cursor: pointer;
}
.leftside-container > svg {
  margin-top: 60px;
}
.rightside-container {
  border-top-left-radius: 100px;
  border-bottom-left-radius: 100px;
  background-color: #eeeeee;
  text-align: right;
  padding-right: 30px;
  cursor: pointer;
}
.rightside-container > svg {
  margin-top: 60px;
}
.linkToRecommendButton {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border: none;
}
.linkToRecommendButton > svg {
  cursor: pointer;
  transition: transform 0.3s ease; /* Add smooth transition for transform */
}
.linkToRecommendButton > svg:hover {
  transform: scale(1.2); /* Scale the image to 1.2 times its original size */
}
.linkToRecommendButton > p {
  margin-top: 20px;
}
strong {
  color: #0092ca;
  font-weight: bold;
  font-size: 20px;
}
.black-font {
  color: black;
  font-size: 20px;
  margin-top: 40px;
}
.button-link-title {
  margin-top: 15px;
  font-size: 20px;
}
</style>