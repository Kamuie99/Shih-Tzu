import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

const API_URL = import.meta.env.VITE_APP_AUTH_API_URL
const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,20}$/;

export const useAuthStore = defineStore('auth', {
  state: () => ({
    token: null,
    isAuthenticated: false,
    user: null,
    userInfo: null,
  }),
  actions: {
    async register(username, password1, password2) {
      try {
        await axios.post(`${API_URL}auth/registration/`, {
          username,
          password1,
          password2
        })
        await this.login(username, password1)
      } catch (err) {
        throw new Error('Registration failed')
      }
    },
    async login(username, password) {
      try {
        const response = await axios.post(`${API_URL}auth/login/`, {
          username,
          password
        })
        this.token = response.data.key
        this.isAuthenticated = true
        this.user = username
        localStorage.setItem('token', this.token)
        axios.defaults.headers.common['Authorization'] = `Token ${this.token}`
      } catch (err) {
        if (err.response) {
          console.error('Server responded with status code:', err.response.status);
          console.error('Response data:', err.response.data);
          const errorMessage = err.response.data.detail || 'Login failed';
          throw new Error(errorMessage);
        } else if (err.request) {
          console.error('No response received:', err.request);
          throw new Error('No response received from server');
        } else {
          console.error('Error setting up request:', err.message);
          throw new Error('Error setting up request');
        }
      }
    },
    logout(router) {
      this.token = null
      this.isAuthenticated = false
      this.user = null
      localStorage.removeItem('token')
      delete axios.defaults.headers.common['Authorization']
      router.push('/')
    },
    checkAuth() {
      const token = localStorage.getItem('token')
      if (token) {
        this.token = token
        this.isAuthenticated = true
        axios.defaults.headers.common['Authorization'] = `Token ${token}`
      } else {
        this.isAuthenticated = false
      }
    },
    async profile(username) {
      try {
        const response = await axios.get(`${API_URL}accounts/${username}`, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        })
        return response.data;
      } catch (error) {
        console.error('Error fetching profile:', error)
      }
    },
    async checkFollowed(username) {
      try {
        const response = await axios.get(`${API_URL}accounts/follow/check/${username}`, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        });
        return response.data.is_followed;
      } catch (error) {
        console.error('Error fetching follow status', error);
        throw error;
      }
    },
    async toggleFollow(username) {
      try {
        const res = await axios.post(`${API_URL}accounts/follow/${username}`, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        });
        return res.data.followed;
      } catch (error) {
        console.error('Error following user', error);
        throw error;
      }
    },
    async updateProfile(formData) {
      try {
        const res = await axios.post(`${API_URL}accounts/update/`, formData, {
          headers: {
            'Authorization': `Token ${this.token}`,
            'Content-Type': 'multipart/form-data'
          }
        })
        return res.data
      } catch (error) {
        console.error('Error updating user', error)
        throw error;
      }
    },
    async changePassword(currentPassword, newPassword1, newPassword2) {
      try {
        await axios.post(`${API_URL}accounts/change-password/`, {
          current_password: currentPassword,
          new_password1: newPassword1,
          new_password2: newPassword2
        }, {
          headers: {
            'Authorization': `Token ${this.token}`
          }
        })
      } catch (err) {
        if (err.response) {
          console.error('Server responded with status code:', err.response.status);
          console.error('Response data:', err.response.data);
          const errorMessage = err.response.data.detail || 'Password change failed';
          throw new Error(errorMessage);
        } else if (err.request) {
          console.error('No response received:', err.request);
          throw new Error('No response received from server');
        } else {
          console.error('Error setting up request:', err.message);
          throw new Error('Error setting up request');
        }
      }
    },
    async deleteUser(username) {
      try {
        const res = await axios.delete(`${API_URL}accounts/delete/${username}/`, {
          headers: {
            'Authorization': `Token ${this.token}`,
          }
        })
      } catch (error) {
        console.error('Error updating user', error)
        throw error;
      }
    }
  },
  persist: true,
})