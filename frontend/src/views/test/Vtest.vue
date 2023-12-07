<script setup>
import DrinkPic from "@/components/DrinkPic.vue";
import { useRoute } from 'vue-router'
const route = useRoute();
const name = route.query.liquid
</script>

<template>
  <div class="fullscreen">
    <Menu></Menu>
    <DrinkPic :liquid=name></DrinkPic>

  </div>

</template>

<style>
</style>