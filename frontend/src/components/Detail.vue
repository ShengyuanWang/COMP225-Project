<script setup>
// set up the props for passing in variables
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  rating: Number, // the rating for the matching drink
  instruction: Array // the instructions for how to make the drink
})

</script>

<template>
  <!--  detailed drink starts here-->
  <div class="pic">
    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload"/>
  </div>
  <div class="pic">
    <div class="name"><h1>{{ props.name }}</h1></div>
    <div class="instruction">
      <ul>
        <li v-for="ins in instruction">{{ins}}</li>
      </ul>
    </div>
    <div class="description">
      <p>Description (bobobobobobobobobobobobobob)</p>
      <p>(bobobobobobobobobobobobobob)</p>
      <p>(bobobobobobobobobobobobobob)</p>
    </div>
  </div>
  <!--  detailed drink ends here-->
</template>

<style scoped>
.pic {
  background-color: #e0ceb4;
  width: 50%;
  height: 100%;
  padding: 20px;
  opacity: 0.9;
  //box-shadow: 10px -5px 5px #968163;
}
.name {
  margin-top: 10px;
  font-size: 50px;
  font-weight: normal;
  color: #992e22;
}
.instruction {
  margin-top: 5px;
  font-size: 20px;
  font-weight: bolder;
  margin-left: 20px;
  color: black;
}
h2 {
  font-size: 30px;
  font-weight: normal;
}
.description {
  margin-left: 40px;
  margin-top: 10px;
  font-size: 20px;
  color: black;
}
h1 {
  font-size: 80px;
}
.btns {
  width: 250px;
  height: 50px;
  position: absolute;
  right: 20px;
  bottom: 50px;
}
.btn {
  height: 50px;
  width: 50px;
  margin-right: 25px;
}
</style>