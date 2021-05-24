<template>
  <div>
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
        <button @click.prevent="login" type="submit" class="btn btn-primary">로그인</button>
      </form>
    </div>
  </div>
  
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      userInfo: {
        username: '',
        password: '',
      
      },
    }
  },
  methods: {
    onClick() {
      this.$store.dispatch('AUTH_USER', this.userInfo)
      .then(() => {
        this.$router.push('/home')
      })
    }
  }
}
</script>

<style>

</style>