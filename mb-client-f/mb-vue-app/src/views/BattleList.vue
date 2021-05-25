<template>
  <div>
    <h1>배틀 목록페이지</h1>
    <BattleVote
      v-for="(movie, index) in movieList"
      :movie="movie"
      :index="index"
      :key="movie.id"
    />

  </div>
</template>

<script>
import BattleVote from '@/components/BattleVote'
export default {
  name: 'BattleList',
  components: {
    BattleVote,
  },
  computed: {
    movieList() {
      return this.$store.getters.getMovieList
    }
  },

  async created() {
    this.$store.dispatch('FETCH_BATTLE_LIST')
  }

}
</script>

<style>

</style>