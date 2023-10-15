<script setup>
const props = defineProps({
  name: String,
  instruction: String
})
</script>

<template>
  <div class="drink-item">
    <div class="drink-image"> <el-image src="src/assets/images/drink.png" fit="cover"/></div>
    <div class="drink-instructions">
      <div class="drink-name">
        {{props.name}}
      </div>
      <div class="instruction">
        {{props.instruction}}
<!--        <p>- 20z.burbon whiskey</p>-->
<!--        <p>- 20z.burbon whiskey</p>-->
<!--        <p>- 20z.burbon whiskey</p>-->
<!--        <p>- 20z.burbon whiskey</p>-->
      </div>

    </div>
  </div>
</template>

<style scoped>
.drink-item {
  width: 340px;
  height: 560px;
  background-color: blue;
  margin: 10px;
}
.drink-image {
  width: 100%;
  height: 350px;
  background-color: green;
  padding: 10px;
}
.drink-instructions {
  width: 100%;
  height: 200px;
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