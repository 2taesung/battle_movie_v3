<template>
  <div>
    <h1>상세페이지</h1>
    <h2>{{ postbattle }}</h2>
    
    
  </div>
</template>

<script>
export default {
  name: 'BattleDetail',
  computed: {
    postbattle() {
      return this.$store.state.postbattle
    }
  },

  // async created() {
  //   return targetbattle = this.$store.state.postbattle
  // }


}
</script>

<style>

</style>