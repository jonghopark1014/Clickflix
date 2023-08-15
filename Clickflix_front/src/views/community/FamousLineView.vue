<template>
  <div>
    <h1>FamousLine</h1>
    <router-link :to="{name:'FamousLineCreate'}">명대사 등록</router-link>
    <FamousLineList />
  </div>
</template>

<script>
import FamousLineList from '@/components/famousline/FamousLineList'

export default {
  name: 'FamousLineView',
  components: {
    FamousLineList,
  },
}
</script>

<style>

</style>