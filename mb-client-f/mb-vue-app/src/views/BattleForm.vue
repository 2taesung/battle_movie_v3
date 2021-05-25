<template>
  <div>
    <h1>배틀생성페이지</h1>
    <!-- <BattleCreateForm/> -->
    <div>
      
      <div class="mb-3">
        <label for="title" class="form-label">제목</label>
        <br>
        <input v-model="battle_info.title" type="text" class="form-control" id="title">
      </div>
    
    
      <div class="mb-3 signup-form">
        <label for="first_movie" class="form-label">영화 1</label>
        <input v-model="battle_info.movie_title_1" type="text" class="form-control" id="first_movie">
        
      </div>
      <div class="mb-3 signup-form">
        <label for="second_movie" class="form-label">영화 2</label>
        <input v-model="battle_info.movie_title_2" type="text" class="form-control" id="second_movie">
      </div>
      <br>

      <button v-on:click.prevent="make" class="btn btn-primary">Submit</button>
      

    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import BattleCreateForm from '@/components/BattleCreateForm'

export default {
  name: 'BattleForm',
  data() {
    return {
      battle_info: {
        title: '',
        movie_title_1: '',
        movie_title_2: '',
      }
    }
  },
  methods: {
    make: function() {
      const token = localStorage.getItem('jwt')
      axios.defaults.headers.common['Authorization'] = `JWT ${token}`
      axios({
        method: 'POST',
        url: 'http://localhost:8000/api/v1/community/community_create/',
        data: this.battle_info
      })
        .then(res => {
          console.log(res)
          // this.$router.push({ name: 'Login' })
        })
        .catch(err => {
          console.log(err)
        })
    }
  }

}
</script>

<style>
  .signup-form {
  display: inline-block;
  margin-right: 10px;
  }

  #title {
    display: inline-block;
    /* margin-right: 100px; */
    width: 40%;
  }
</style>