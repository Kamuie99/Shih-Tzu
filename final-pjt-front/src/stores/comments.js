import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import { useAuthStore } from './auth'
import axios from 'axios'


const API_URL = import.meta.env.VITE_APP_COMMNET_API_URL
export const useCommentStore = defineStore('comments', () => {
  const authStore = useAuthStore()
  const comments = ref([])

  const getComments = async (movieId) => {
    try {
      const res = await axios.get(`${API_URL}reviews/${movieId}`);
      comments.value = res.data;
    } catch (error) {
      console.error('Error fetching movies:', error);
    }
  };
  
  const commentSubmit = async (movieId, commentText) => {
    try {
      await axios.post(`${API_URL}reviews/${movieId}`, {
        content: commentText,
        movie: movieId,
        headers: {
          'Authorization': `Token ${authStore.token}`
        }
      });
      await getComments(movieId);
    } catch (error) {
      console.error('Error submitting comment:', error);
      throw error;
    }
  };

  const commentDelete = async (movieId, commentId) => {
    try {
      await axios.delete(`${API_URL}reviews/delete/${commentId}`, {
        headers: {
          'Authorization': `Token ${authStore.token}`
        }
      });
      await getComments(movieId);
    } catch (error) {
      console.error('Error deleting comment:', error)
      throw error;
    }
  };
  return { comments, getComments, commentSubmit, commentDelete }
}, {persist: true})
