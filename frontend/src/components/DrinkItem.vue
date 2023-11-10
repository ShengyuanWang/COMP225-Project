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
    <div class="drink-image"> <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload"/></div>
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
  width: 360px;
  height: 650px;
  margin-top: 20px;
  margin-right: 20px;
  box-shadow: 10px 5px 6px #968163;
}
.drink-image {
  width: 100%;
  height: 370px;
  background-color: #D8C3A5;
  padding: 10px;
}
.drink-instructions {
  width: 100%;
  height: 280px;
  background-color: #c2ae91;
  padding: 10px;
}
.drink-name {
  font-size: 25px;
  color: #992e22;
  font-weight: bold;
}
.instruction {
  color: black;
  font-size: 15px;
  padding-top: 10px;
  padding-left: 20px;
}

</style>