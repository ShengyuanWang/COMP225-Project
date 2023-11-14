<script setup>
// set up props for Drink items
const props = defineProps({
  name: String, // the name of the drink
  instruction: String, // the instruction about how to make the drink
  url: String // the url for the image of the drink
})
</script>

<template>
  <div class="drink-item">
    <div class="drink-image"> <img :src="props.url" alt="Alcohol Image Onload"/></div>
    <div class="drink-instructions">
      <h1 class="drink-name">
        {{ props.name }}
      </h1>
      <div class="instruction">
        <ul>
          <li v-for="item in props.instruction">{{ item }}</li>
        </ul>
      </div>

    </div>
  </div>
</template>

<style scoped>
.drink-item {
  width: 20vw;
  height: 65vh;
  margin-top: 2vh;
  margin-right: 1vw;
  box-shadow: 1vh 0.5vh 0.5vh #968163;
}
.drink-image {
  width: 100%;
  height: 35vh;
  background-color: #D8C3A5;
  padding: 1vh;
  text-align: center;
}

img {
  height: 100%;
  aspect-ratio: 1/2;
}

.drink-instructions {
  width: 100%;
  height: 30vh;
  background-color: #c2ae91;
  padding: 1vh;
}
.drink-name {
  font-size: 1.5vw;
  color: #992e22;
  font-weight: bold;
}
.instruction {
  color: black;
  font-size: 1.5vh;
  padding-top: 1vh;
  padding-left: 1vw;
}

</style>