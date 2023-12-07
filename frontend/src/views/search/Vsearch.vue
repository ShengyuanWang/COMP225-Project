<template>

  <div class="fullscreen">
    <Menu @childClick="childValFn"></Menu>
    <div class="search">
      <Qinput move place="350" place-holder="Please type in the book name"></Qinput>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue';
const childData = ref(null)
// 父组件传递过来事件
const childValFn = (e)=>{
  //接收子组件传递给父组件的值
  childData.value = e.value
  console.log(childData.value);
  // for (child of childData.value) {
  //   console.log(child)
  // }
}
</script>

<style scoped>
.search {
  display: flex;
  position: relative;
}
</style>
