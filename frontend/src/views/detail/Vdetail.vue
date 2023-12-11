<script setup>
// import the required packages
import Qinput from "@/components/Qinput.vue";
import { useRoute } from 'vue-router'
import {onMounted} from "vue";
const route = useRoute()

// get the data from route url
let name = route.query.name;
let instructions = route.query.instructions;
let ingredients = route.query.ingredients;
let genres = route.query.genres;
let image = route.query.liquid;



</script>

<template>

  <div class="fullscreen">
    <Menu></Menu>
    <div class="header">
      <Qinput place="40"></Qinput>
    </div>
    <div class="match_result">
      <Detail url="https://i.ibb.co/989gpGR/drink1.png"
              :name=name
              :instructions=instructions
              :ingredients=ingredients
              :genres=genres
              :image=image>
      </Detail>
    </div>

  </div>
</template>

<style>
.header {
  height: 6ch;
  width: 100%;
}

.match_result {
  width: 80vw;
  height: 85vh;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw;
}
</style>