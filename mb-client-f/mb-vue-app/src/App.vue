<template>
  <div id="app">
    <div id="nav">
      <ul>
        <div v-if="!isLogin">

          <router-link :to="{ name:'login' }">로그인</router-link>|
          <router-link :to="{ name:'signup' }">회원가입</router-link>|

        </div>
        <div v-else>
          <router-link :to="{ name:'home' }">home</router-link>| 
          <router-link :to="{ name: 'battleform' }">배틀생성</router-link>|
          <router-link :to="{ name: 'battlelist' }">배틀목록</router-link>
        </div>
      </ul>
    </div>

    
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
    }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    if (token) {
      this.isLogin = true
    }
  }

}
</script>

<style>
  @import "https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css";

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #ffffff;
}

#nav {
  padding: 30px;
  display: flex;
  justify-content: center;
  /* border: 5px solid red; */
}

ul {
  display: flex;
  justify-content: center;
  align-content: center;
  border: 5px solid red;
  border-radius: 100px;
  width: 40%;
  height: 50px;
  margin: 10px;
  border-radius: 0%;
  font-size: 30px;
}

#nav a {
  font-weight: bold;
  color: #ffffff;
}

#nav a.router-link-exact-active {
  color: #ff0000;
}

body {
	margin:0;
	padding:0;
	background-color:#222;
}

</style>
