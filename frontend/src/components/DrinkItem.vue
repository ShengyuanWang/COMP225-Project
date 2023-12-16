<script setup>
import {ref} from "vue";
import DrinkPic from "@/components/DrinkPic.vue";
// set up props for Drink items
const props = defineProps({
  name: String, // the name of the drink
  ingredients: Array, // the instruction about how to make the drink
  instructions: String, // the instruction about how to make the drink
  description: String,
  url: String, // the url for the image of the drink
  liquid: String
})

const image = ref('')
if (props.liquid === 'TBA') {
  image.value = 'blackMagic'
} else {
  image.value = props.liquid
}

console.log(image.value)
</script>

<template>
  <div class="drink-item">
<!--    <div class="drink-image"> <img :src="props.url" alt="Alcohol Image Onload"/></div>-->
    <div class="drink-image"> <DrinkPic :liquid=image style="height: 100%; text-align: left;"></DrinkPic></div>
    <div class="drink-instructions">
      <h1 class="drink-name">
        {{ props.name }}
      </h1>
      <div class="instruction">
        <p>{{ props.description }}</p>
      </div>
    </div>
  </div>
</template>

<style>
.drink-item {
  width: 20vw;
  height: 65vh;
  margin-top: 2vh;
  margin-right: 1vw;
  box-shadow: 1vh 0.5vh 0.5vh #968163;
}

.drink-item:hover {
  box-shadow: 1vh 0.5vh 0.5vh #111111;
}

.drink-image {
  width: 100%;
  height: 35vh;
  background-color: #000435;
  padding: 1vh;
  text-align: left;
}

img {
  height: 100%;
  aspect-ratio: 1/2;
}

.drink-instructions {
  width: 100%;
  height: 30vh;
  background-color: #dba858;
  padding: 1vh;
}

.drink-name {
  font-size: 1.5vw;
  color: #8c0e0f;
  font-weight: bold;
}

.instruction {
  color: black;
  font-size: 1.5vh;
  padding-top: 1vh;
  padding-left: 1vw;
}
</style>