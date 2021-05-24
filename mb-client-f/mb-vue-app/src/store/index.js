import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

// axios.defaults.baseURL = 'http://localhost:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    movielist: [],
  },
  getters: {
    getMovieList(state) {
      return state.movielist
    }
  },
  mutations: {
    FETCH_MOVIE_LIST(state, movielist){
      state.movielist = movielist
    }
  },
  actions: {
    async FETCH_MOVIE_LIST({ commit }) {
      const MOVIE_LIST_URL = 'http://localhost:8000/api/v1/community/'
      const response = await axios.get(MOVIE_LIST_URL)
      const movielist = response.data
      // console.log(movielist)
      commit('FETCH_MOVIE_LIST', movielist)
    }
    
  },
  modules: {
  }
})
