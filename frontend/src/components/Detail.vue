<script setup>
const props = defineProps({
  url: String,
  name: String,
  rating: Number,
  instruction: Array
})

</script>

<template>
  <div class="pic">
    <el-image :src="props.url" fit="cover"/>
  </div>
  <div class="detail">
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
    <div class="btns">
      <span class="btn"><el-icon :size="50" color="White"><Download /></el-icon></span>
      <span class="btn"><el-icon :size="50" color="White"><Share /></el-icon></span>
      <span class="btn"><el-icon :size="50" color="White"><Refresh /></el-icon></span>
    </div>

  </div>
</template>

<style scoped>
.pic {
  background-color: pink;
  width: 50%;
  height: 100%;
  padding: 20px;
}
.detail {
  background-color: gray;
  width: 50%;
  height: 100%;
  padding: 20px;
}
.name {
  margin-top: 10px;
  font-size: 50px;
  font-weight: normal;
  color: black;
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