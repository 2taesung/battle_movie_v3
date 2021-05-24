import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

// axios.defaults.baseURL = 'http://localhost:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movielist: [],
    userInfo: {},
  },
  getters: {
    getMovieList(state) {
      return state.movielist
    }
  },
  mutations: {
    FETCH_MOVIE_LIST(state, movielist){
      state.movielist = movielist
    },
    CREATE_USER(state, userInfo) {
      state.userInfo = userInfo
    },
  },
  actions: {
    async FETCH_MOVIE_LIST({ commit }) {
      const MOVIE_LIST_URL = 'http://localhost:8000/api/v1/community/'
      const response = await axios.get(MOVIE_LIST_URL)
      const movielist = response.data
      // console.log(movielist)
      commit('FETCH_MOVIE_LIST', movielist)
    },
    async CREATE_USER({ commit }, userInfo) {
      const USER_CREATE_URL = 'http://localhost:8000/api/v1/accounts/signup/'
      const data = userInfo
      const response = await axios.post(USER_CREATE_URL, data)

      console.log(response)
      
      commit('CREATE_USER', response.data)
    },
    
  },
  modules: {
  }
})
