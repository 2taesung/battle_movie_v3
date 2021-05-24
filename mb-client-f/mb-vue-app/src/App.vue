<template>
  <div id="app">
    <div id="nav">
      <ul>
        <router-link :to="{ name:'Home' }">Home</router-link>| 
        <router-link :to="{ name:'login' }">로그인</router-link>|
        <router-link :to="{ name:'signup' }">회원가입</router-link>|
        <router-link :to="{ name: 'battleform' }">배틀 생성하기</router-link>|
        <router-link :to="{ name: 'battlelist' }">목록보기</router-link>
      </ul>
    </div>

    <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-inner">


      </div>
    </div>
    <router-view/>
  </div>
</template>

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
