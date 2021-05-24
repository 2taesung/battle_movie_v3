<template>
  <div>회원가입폼
    <form>
      <div class="mb-3">
        <label for="username" class="form-label">Username</label>
        <input v-model="userInfo.username" type="text" class="form-control" id="username" aria-describedby="emailHelp">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input v-model="userInfo.password" type="password" class="form-control" id="password">
      </div>
      <div class="mb-3">
        <label for="password-confirmation" class="form-label">Password Confirmation</label>
        <input v-model="userInfo.password_confirmation" type="password" class="form-control" id="password-confirmation">
      </div>
      <button @click.prevent="signup(userInfo)" type="submit" class="btn btn-primary">회원가입</button>
    </form>

  </div>
</template>

<script>


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
      signup(){
        this.$store.dispatch('CREATE_USER', this.userInfo)
      }
  }

}
</script>

<style>

</style>