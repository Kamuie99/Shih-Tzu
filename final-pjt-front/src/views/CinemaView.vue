<template>
  <section class="cinema">
    <div class="cinema-title">
      <strong>|</strong><p> 근처 <strong>영화관</strong> 검색</p>
    </div>
    <div class="map-container">
      <div id="map"></div>
      <div class="button-result">
        <div class="Cinema-select">
          <div
            class="cinema-button megabox-btn"
            :class="{ active: selectedKeyword === '메가박스', inactive: selectedKeyword && selectedKeyword !== '메가박스' }"
            @click="selectedKeyword='메가박스'; searchPlaces(selectedKeyword);"
          >
            <img src="@/assets/images/Logo_Mega.png" width="120px" height="20px">
          </div>
          <div
            class="cinema-button lottecinema-btn"
            :class="{ active: selectedKeyword === '롯데시네마', inactive: selectedKeyword && selectedKeyword !== '롯데시네마' }"
            @click="selectedKeyword='롯데시네마'; searchPlaces(selectedKeyword);"
          >
            <img src="@/assets/images/Logo_Lotte.png" width="120px" height="30px">
          </div>
          <div
            class="cinema-button cgv-btn"
            :class="{ active: selectedKeyword === 'CGV', inactive: selectedKeyword && selectedKeyword !== 'CGV' }"
            @click="selectedKeyword='CGV'; searchPlaces(selectedKeyword);"
          >
            <img src="@/assets/images/Logo_CGV.png" width="70px" height="30px" />
          </div>
        </div>
        <div class="result-container" v-if="selectedKeyword !== null">
          <div class="place-list" v-if="places.length > 0" style="font-size: 17px;">
            <ul>
              <li v-for="(place, index) in places" :key="place.id" @click="clickPlace(index)" :class="{ active: selectedPlaceIndex === index }" style="cursor: pointer;" class="placeToClick"><strong>|</strong> {{ place.place_name }}</li>
            </ul>
          </div>
          <div class="place-list _2" style="width:200px; margin-top: 50px;" v-else>근처에 영화관이 없어요</div>
        </div>
        <div class="place-list _2" style="width: 200px; margin-top: 50px;" v-else>영화관을 선택해주세요</div>
      </div>
    </div>
  </section>
</template>

<script>
const map_api_key = import.meta.env.VITE_APP_MAP_API_KEY;
export default {
  name: "CinemaView",
  data() {
    return {
      latitude: null,
      longitude: null,
      map: null,
      infowindow: null,
      ps: null,
      initialZoomLevel: 8,
      initialCenter: { lat: 35.15165, lng: 129.0430 },
      selectedKeyword: null,
      markers: [],
      places: [],
      selectedPlaceIndex: null,
    };
  },

  mounted() {
    this.loadKakaoMapScript();
  },
  
  methods: {
    loadKakaoMapScript() {
      if (window.kakao && window.kakao.maps) {
        this.initMap();
      } else {
        const script = document.createElement("script");
        script.onload = () => kakao.maps.load(this.initMap);
        script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${map_api_key}&libraries=services&autoload=false`;
        document.head.appendChild(script);
      }
    },

    initMap() {
      this.createMap();
    },

    createMap() {
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });
      var mapContainer = document.getElementById("map");
      this.map = new kakao.maps.Map(mapContainer, {
        center: new kakao.maps.LatLng(this.initialCenter.lat, this.initialCenter.lng),
        level: this.initialZoomLevel,
      });
      this.ps = new kakao.maps.services.Places();

      kakao.maps.event.addListener(this.map, "dragend", () => {
        this.searchPlaces(this.selectedKeyword);
      });
    },
    
    searchPlaces() {
      if (!this.selectedKeyword) return;

      const bounds = this.map.getBounds();
      const zoomLevel = this.map.getLevel();
      const center = this.map.getCenter();
      const radius = this.calculateRadius();

      const options = {
        bounds: bounds,
        category_group_code: 'CT1',
      };

      this.removeMarkers();
      this.places = [];
      this.selectedPlaceIndex = null;

      this.ps.keywordSearch(
        this.selectedKeyword,
        (data, status, pagination) => {
          if (status === kakao.maps.services.Status.OK) {
            const bounds = new kakao.maps.LatLngBounds();
            data.forEach((place) => {
              if (place.category_group_code === 'CT1') {
                this.displayMarker(place);
                bounds.extend(new kakao.maps.LatLng(place.y, place.x));
                this.places.push(place)
              }
            });

            this.map.setLevel(zoomLevel, { animate: false });
            this.map.panTo(center);
          }
        },
        options
      );
    },

    calculateRadius() {
      const zoomLevel = this.map.getLevel();
      const baseRadius = 1000;
      const maxRadius = 20000;
      const radius = baseRadius * zoomLevel/2;
      return Math.min(radius, maxRadius);
    },

    displayMarker(place) {
      const marker = new kakao.maps.Marker({
        map: this.map,
        position: new kakao.maps.LatLng(place.y, place.x),
      });
      marker.getTitle();
      this.markers.push(marker);

      kakao.maps.event.addListener(marker, "click", () => {
        const content = `
          <div style="padding:5px;font-size:12px;">
            <a href="${place.place_url}" target="_blank" style="text-decoration:none;color:inherit;">${place.place_name}</a>
          </div>`;
        this.infowindow.setContent(content);
        this.infowindow.open(this.map, marker);
      });
    },

    removeMarkers() {
      this.markers.forEach(marker => marker.setMap(null));
      this.markers = [];
    },

    clickPlace(index) {
      this.selectedPlaceIndex = index;
      const marker = this.markers[index];
      kakao.maps.event.trigger(marker, 'click');
      this.map.panTo(marker.getPosition());
    },
  },
};
</script>

<style scoped>
.cinema {
  width: 100%;
  height: 92vh;
  display: flex;
  flex-direction: column;
}

.map-container {
  display: flex;
  align-items: center;
  justify-content: space-around;
  flex-direction: row;
  width: 100%;
  height: 80vh;
}
#map {
  width: 60%;
  height: 74vh;
  border: 6px #0092ca solid;
  border-radius: 12px;
  overflow: hidden;
  margin: 40px;
}
.place-list {
  color: white;
  display: flex;
  font-size: 18px;
}
.place-list li {
  margin-bottom: 1rem;
}
.button-result {
  width: 30%;
  height: 100%;
}
.Cinema-select {
  display: flex;
  justify-content: space-around;
  align-items: center;
  margin: 20px;
  width: 400px;
  padding: 20px;
  border: 3px solid #0092ca;
  border-radius: 10px;
}

.cinema-button {
  transition: transform 0.3s, filter 0.3s, brightness 0.3s;
}
.cinema-button:hover {
  transform: scale(1.1);
  filter: brightness(100%);
}
.cinema-button.inactive:hover {
  filter: brightness(100%);
}
.cinema-button.inactive {
  filter: brightness(20%);
}

.placeToClick:hover {
  color: #0092ca;
}
.placeToClick:active {
  color: #0092ca;
}
.placeToClick.active {
  color: #0092ca;
}
.cinema-title {
  color: white;
  font-size: 25px;
  display: flex;
  align-items: center;
  width: 80%;
  height: 8vh;
  margin-left: 40px;
}
.cinema-title > strong {
  margin-left: 20px;
}
.cinema-title > p {
  margin-left: 10px;
}
.cgv-btn {
  background-image: url('@/assets/images/Logo_CGV.png');
}

.cinema-button > img {
  cursor: pointer;
}
.result-container {
  width: 400px;
  margin-top: 50px;
  margin-left: 20px;
  display: flex;
  justify-content: center;
}
</style>
