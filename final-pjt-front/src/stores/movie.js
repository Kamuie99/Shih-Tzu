import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'
import axios from 'axios'

const API_URL = import.meta.env.VITE_APP_MOVIE_API_URL
export const useMovieStore = defineStore('movie', () => {
  const movies = ref([])
  const genres = ref([])
  const boxOffice = ref([])
  const shihtzuRecommendMovies = ref([])
  const followers = ref([])
  const followings = ref([])
  const comments = ref([])
  const likedMovies = ref([])
  const searchedMovies = ref([])
  const authStore = useAuthStore()
  const AIText = ref('')
  const prompt = ref('')

  const selectedOption = ref('now')
  const preferences = ref({
    time: true,
    where: '',
    withWho: '',
    isWeekend: false,
  })


  const getMovies = async () => {
    if (movies.value.length === 0) {
      try {
        const res = await axios.get(API_URL + 'list/');
        movies.value = res.data;
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    }
  };

  const getGenres = async () => {
    if (genres.value.length === 0) {
      try {
        const res = await axios.get(API_URL + 'genre-list/');
        genres.value = res.data;
      } catch (error) {
        console.error('Error fetching genres:', error)
      }
    }
  }
  
  const getBoxOffice = async() => {
    try {
      const res = await axios.get(API_URL + 'box_office/');
      boxOffice.value = res.data;
    } catch (error) {
      console.error('Error fetching box office:', error);
    }
  };

  const getSimilarMovies = async (movieId) => {
    try {
      const res = await axios.get(API_URL + `similar/${movieId}`);
      return res.data;
    } catch (error) {
      console.error('Error fetching similar Movies:', error)
      return []
    }
  }

  const shihtzuMovies = async (preferences) => {
    try {
      const res = await axios.get(API_URL + 'shihtzu/', {
        params: preferences
      })
      shihtzuRecommendMovies.value = res.data
    } catch (error) {
      console.error('Error fetching shihtzu Movies:', error)
    }
  }

  const submitPreferences = (time, where, withWho, isWeekend) => {
    preferences.value = { time, where, withWho, isWeekend }
  }

  const AIRecommend = async (preferences) => {
    try {
      const res = await axios.get(API_URL + 'AI/', {
        params: preferences
      })
      shihtzuRecommendMovies.value = res.data.movies
      AIText.value = res.data.assistant_reply
    } catch (error) {
      console.error('Error fetching AI Recommended Movies:', error)
    }
  }

  const toggleLike = async (movieId) => {
    try {
      const res = await axios.post(API_URL + `like/${movieId}`, {
        headers: {
          'Authorization': `Token ${authStore.token}`
        }
      });
      return res.data.liked;
    } catch (error) {
      console.error('Error toggling like:', error);
      throw error;
    }
  }

  const checkLiked = async (movieId) => {
    try {
      const res = await axios.get(API_URL + `like/${movieId}`, {
        headers: {
          'Authorization': `Token ${authStore.token}`,
        }
      });
      return res.data.liked;
    } catch (error) {
      console.error('Error checking if movie is liked:', error);
      throw error;
    }
  };

  const searchMovies = async (query, genreId) => {
    const store = useMovieStore();
    
    try {
      const movies = store.movies;
  
      const filteredMovies = movies.filter(movie => {
        const matchesQuery = query
          ? movie.title.toLowerCase().includes(query.toLowerCase())
          : true;
        const matchesGenre = !genreId || movie.genres.includes(parseInt(genreId, 10));
        return matchesQuery && matchesGenre;
      });
  
      const nowPlayingMovies = filteredMovies.filter(movie => movie.now_playing);
      const notNowPlayingMovies = filteredMovies.filter(movie => !movie.now_playing);
  
      searchedMovies.value = filteredMovies;
  
      return {
        nowPlayingMovies,
        notNowPlayingMovies
      };
  
    } catch (error) {
      console.error('Error filtering movies:', error);
      throw error;
    }
  }

  return { movies, genres, boxOffice, selectedOption, preferences, shihtzuRecommendMovies, followers, followings, comments, likedMovies, searchedMovies, AIText, prompt, getMovies, getGenres, getBoxOffice, getSimilarMovies, shihtzuMovies, submitPreferences, AIRecommend, toggleLike, checkLiked, searchMovies}
}, {persist: true})