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
        <div class="carousel-item active">
          <img src="@/assets/logo.png/" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/logo.png/" class="d-block w-100" alt="...">
        </div>
        <div class="carousel-item">
          <img src="@/assets/logo.png/" class="d-block w-100" alt="...">
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <router-view/>
  </div>
</template>

<style>
@import "https://cdn-css-file.css";
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
