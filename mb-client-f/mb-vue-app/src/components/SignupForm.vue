<template>
  <div class="d-flex justify-content-center flex-column">
    <form class="d-flex align-items-center justify-content-center flex-column">
      <div class="mb-3 signup-form">
        <label for="username" class="form-label">Username</label>
        <input v-model="userInfo.username" type="text" class="form-control" id="username" aria-describedby="emailHelp">
      </div>
      
      <div class="mb-3 signup-form">
        <label for="password" class="form-label">Password</label>
        <input v-model="userInfo.password" type="password" class="form-control" id="password">
      </div>
      <div class="mb-3 signup-form">
        <label for="password-confirmation" class="form-label">Password Confirmation</label>
        <input v-model="userInfo.password_confirmation" type="password" class="form-control" id="password-confirmation">
      </div>
      <button @click.prevent="signup" type="submit" class="btn btn-primary">회원가입</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'SignupForm',
  data() {
    return {
      userInfo: {
        username: '',
        password: '',
        password_confirmation: '',
      }
    }
  },
  methods: {
      // signup(){
      //   this.$store.dispatch('CREATE_USER', this.userInfo)
      // }
      signup: function() {
        axios({
          method: 'POST',
          url: 'http://localhost:8000/api/v1/accounts/signup/',
          data: this.userInfo
        })
          .then(res => {
            console.log(res)
            this.$router.push({ name: 'Login' })
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
/* @import "https://cdn-css-file.css"; */
</style>