<script setup>
// set up the props for passing in variables
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  rating: Number, // the rating for the matching drink
  instruction: Array, // the instructions for how to make the drink
  description: String,
})

</script>

<template>
  <!--  detailed drink starts here-->
  <div class="pic">
    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload"/>
  </div>
  <div class="pic">
    <div class="name"><h1>{{ props.name }}</h1></div>
<!--    <div class="instruction">-->
<!--      <ul>-->
<!--        <li v-for="ins in instruction">{{ins}}</li>-->
<!--      </ul>-->
<!--    </div>-->
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
  //box-shadow: 10px -5px 5px #968163;
}
.name {
  margin-top: 1vh;
  font-size: 3vw;
  font-weight: normal;
  color: #992e22;
}
.instruction {
  margin-top: 0.5vh;
  font-size: 1.4vw;
  font-weight: bolder;
  margin-left: 1vw;
  color: black;
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
h1 {
  font-size: 5vw;
}

</style>