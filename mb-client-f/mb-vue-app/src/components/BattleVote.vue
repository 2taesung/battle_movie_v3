<template>
  <div class="d-flex justify-content-center">
    
    <ul>
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
  }

}
</script>

<style>

</style>