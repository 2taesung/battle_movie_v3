<template>
  <div>
    <h2>왼쪽</h2>
    <form>
      <div class="mb-3">
        <input v-model="leftmovie.title" placeholder="영화 제목" class="form-control">
      </div>
 
      <button type="submit" class="btn btn-primary">입력</button>
    </form>
    
  </div>
</template>

<script>
export default {
  name: 'LeftMovie',
  data() {
    return {
      leftmovie: {
        title: '',
      }
    }
  },

}
</script>

<style>
  .signup-form {
  display: inline-block;
  margin-right: 10px;
  }
</style>