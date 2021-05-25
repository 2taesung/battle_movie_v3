<template>
  <div>
    <h1>배틀 목록페이지</h1>
    <BattleVote
      v-for="(battle, index) in battleList"
      :battle="battle"
      :index="index"
      :key="battle.id"
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
    battleList() {
      return this.$store.getters.getBattleList
    }
  },

  async created() {
    this.$store.dispatch('FETCH_BATTLE_LIST')
  }

}
</script>

<style>

</style>