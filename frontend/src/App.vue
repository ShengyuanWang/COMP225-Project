<script setup>
import {useRoute} from "vue-router";
const route = useRoute()
</script>

<template>
<div class="fullscreen">
  <Menu></Menu>
  <router-view :key="route.fullPath"></router-view>
</div>
</template>

<style scoped>
.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100vw;
  height: 100vh;
  background-color: #EAE7DC;
}
</style>
