<template>
  <div>
    <hr style="height: 8px;">
    <div>
    <h1>
    배틀 목록페이지
    </h1>
    <button style="float:right; width:150px;">배틀생성</button>
    <br>
    </div>
    <hr style="height: 5px;">
    <br>
    <br>
    <br>
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

<style scoped>
hr {
  background-color: red ;
}
</style>
