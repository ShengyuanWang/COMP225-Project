<script setup>
import DrinkPic from "@/components/DrinkPic.vue";
import { useRoute } from 'vue-router'
const route = useRoute();
const name = route.query.liquid
</script>

<template>
  <DrinkPic :liquid=name></DrinkPic>
</template>

<style>
</style>