<template>
  <div>
    <h2>목록을 누르면</h2>
    <ul>
      <li>
      {{ movie.title }}
      </li>
    </ul>

    <!-- <span>{{ movie.title }}</span> -->
  </div>
</template>

<script>

export default {
  name: 'BattleVote',
  props: {
    movie: {
      type: Object,
      required: true,
    }
  }
}
</script>

<style>

</style>