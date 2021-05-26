<template>
  <div class="d-flex justify-content-center">
    <ul @click="onClick(battle)">
      {{ battle.title }}
    </ul>
    
  </div>
</template>

<script>
export default {
  name: 'BattleVote',
  props: {
    battle: {
      type: Object,
      required: true,
    }
  },
  methods: {
    onClick(battle) {
      this.$store.commit('DETAIL_POST', battle)
      this.$router.push('/detail')
    }
  }


}
</script>

<style>

</style>