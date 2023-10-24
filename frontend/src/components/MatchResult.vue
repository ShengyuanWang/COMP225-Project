<script setup>
// import required packages
import {ElNotification} from "element-plus";
import { h } from 'vue'

// set up props for matching result
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of drink item
  rating: Number // the rating for the match
})

// handling the click action for the download icon
const clickDownload = () => {
  console.log('Click Download')
  ElNotification({
    title: 'Download Finish',
    message: h('i', { style: 'color: teal' }, 'You have successfully download the matching result'),
  })
}

// handling the click action for the share icon
const clickShare = () => {
  console.log('Click Share')
  ElNotification({
    title: 'Share Finish',
    message: h('i', { style: 'color: teal' }, 'You have successfully share the matching result'),
  })
}

// handling the click action for the change icon
const clickChange = () => {
  console.log('Click Change')
  ElNotification({
    title: 'Change Another?',
    message: h('i', { style: 'color: teal' }, 'You have successfully change another matching result'),
  })
}
</script>

<template>
<div class="pic">
  <el-image :src="props.url" fit="cover"/>
</div>
  <div class="detail">
    <div class="name"><h1>{{ props.name }}</h1></div>
    <div class="rate">
      <h2>Match Rating</h2>
      <el-icon :size="35" v-for="(item, index) in parseInt(props.rating)"><StarFilled /></el-icon>
      <el-icon :size="35" color="white" v-for="(item , index) in 5-parseInt(props.rating)"><StarFilled /></el-icon>
    </div>
    <div class="description">
      <p>Slice the lemon quarter into three wedges. Rinse off a couple sprigs of mint (or just one if foregoing the garnish).
      Throw the mint leaves in a cocktail shaker (I usually use six leaves or so, but adjust to taste). Add the lemon wedges and simple syrup,
      then muddle. Finally, add the whiskey and some ice. Shake vigorously until the shaker is nice and frosty. Strain into a rocks glass filled with ice,
        add the second sprig of mint as a garnish (if desired), and enjoy.</p>
    </div>
    <div class="btns">
      <span class="btn" @click="clickDownload"><el-icon :size="50" color="White"><Download /></el-icon></span>
      <span class="btn" @click="clickShare"><el-icon :size="50" color="White"><Share /></el-icon></span>
      <span class="btn" @click="clickChange"><el-icon :size="50" color="White"><Refresh /></el-icon></span>
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
  padding: 10px;
}
.name {
  margin-top: 120px;
  font-size: 80px;
  font-weight: normal;
  color: black;
}
.rate {
  margin-top: 5px;
  margin-left: 40px;
  color: black;
}

h2 {
  margin-left: 5px;
  font-size: 30px;
  font-weight: normal;
}
.description {
  margin-top: 10px;
  margin-left: 50px;
  width: 500px;
  font-size: medium;
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