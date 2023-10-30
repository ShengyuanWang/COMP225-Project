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
    <div class="drink-image"> <el-image :src="props.url" fit="cover"/></div>
    <div class="drink-instructions">
      <div class="drink-name">
        {{ props.name }}
      </div>
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
  width: 360px;
  height: 650px;
  background-color: blue;
  margin: 10px;
}
.drink-image {
  width: 100%;
  height: 370px;
  background-color: green;
  padding: 10px;
}
.drink-instructions {
  width: 100%;
  height: 280px;
  background-color: purple;
  padding: 10px;
}
.drink-name {
  font-size: 25px;
  color: black;
  font-weight: bold;
}
.instruction {
  color: black;
  font-size: 15px;
  padding-top: 10px;
  padding-left: 20px;
}
</style>