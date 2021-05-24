<template>
  <div>
    <h1>배틀 목록페이지</h1>
    <!-- <span>{{ movieList }}</span> -->
    <!-- <span>
      {{ movieList.movie }}
    </span> -->
    <!-- <li v-for="movie in movieList" :key="movie.id">{{ movie.title }}</li> -->
    <!-- <BattleVote/> -->
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
    this.$store.dispatch('FETCH_MOVIE_LIST')
  }

}
</script>

<style>

</style>