<template>
  <div class="d-flex justify-content-center">

    <LeftMovie/> <RightMovie/>
  </div>

</template>

<script>
import RightMovie from '@/components/RightMovie'
import LeftMovie from '@/components/LeftMovie'

export default {
  name: 'BattleCreateForm',
  components: {
    RightMovie,
    LeftMovie,
  }

}
</script>

<style>

</style>