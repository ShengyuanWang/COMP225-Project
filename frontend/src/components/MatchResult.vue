<script setup>
const props = defineProps({
  url: String
})
</script>

<template>
<div class="pic">
  <el-image :src="props.url" fit="cover"/>
</div>
  <div class="detail">
    <div class="name">Red Wine</div>
    <div class="rate">
      <p>Match Rating</p>
      <el-icon :size="35"><StarFilled /></el-icon>
      <el-icon :size="35"><StarFilled /></el-icon>
      <el-icon :size="35"><StarFilled /></el-icon>
      <el-icon :size="35"><StarFilled /></el-icon>
      <el-icon :size="35" color="white"><StarFilled /></el-icon>
    </div>
    <div class="description">
      <p>Description (bobobobobobobobobobobobobob)</p>
      <p>(bobobobobobobobobobobobobob)</p>
      <p>(bobobobobobobobobobobobobob)</p>
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
  margin-top: 150px;
  font-size: 80px;
  font-weight: normal;
  color: black;
}
.rate {
  margin-top: 20px;
  font-size: 30px;
  color: black;
}
.description {
  margin-top: 10px;
  font-size: medium;
  color: black;
}
</style>