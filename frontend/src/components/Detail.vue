<script setup>
// set up the props for passing in variables
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  rating: Number, // the rating for the matching drink
  instruction: Array, // the instructions for how to make the drink
  description: String, // the description for the drink
})
</script>

<template>
  <!--  detailed drink starts here-->
  <div class="pic">
    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload"/>
  </div>
  <div class="pic">
    <div class="name"><h1>{{ props.name }}</h1></div>
    <div class="description">
      <p style="font-size: 1.2vw;">{{description}}</p>
    </div>
  </div>
  <!--  detailed drink ends here-->
</template>

<style scoped>
.pic {
  background-color: #e0ceb4;
  width: 50%;
  height: 100%;
  padding: 2vh;
  opacity: 0.9;
}

.name {
  margin-top: 1vh;
  font-size: 3vw;
  font-weight: normal;
  color: #992e22;
}

h1 {
  font-size: 5vw;
}

h2 {
  font-size: 2vw;
  font-weight: normal;
}

.description {
  margin-left: 2vw;
  margin-top: 2vh;
  font-size: 1vw;
  color: black;
}
</style>