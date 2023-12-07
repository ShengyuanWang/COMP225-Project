<script setup>
// import required packages
import {ElNotification} from "element-plus";
import { h } from 'vue'

// set up props for matching result
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of drink item
  rating: Number, // the rating for the match
  description: String, // the description for the match
  ingredients: Array,
  notes: String

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
<!--    <div class="rate">-->
<!--      <h2>Match Rating</h2>-->
<!--      <el-icon size="2vw" v-for="(item, index) in parseInt(props.rating)"><StarFilled /></el-icon>-->
<!--      <el-icon size="2vw" color="white" v-for="(item , index) in 5-parseInt(props.rating)"><StarFilled /></el-icon>-->
<!--    </div>-->
    <div class="description">
      <p>{{description}}</p>
    </div>

    <div v-if="ingredients.length >= 1" class="description">
      <p>Ingredients:</p>
      <ul>
        <li v-for="(ingredient, index) in ingredients" :key="index">{{ ingredient }}</li>
      </ul>
    </div>


    <div class="description">
      <p>{{notes}}</p>
    </div>

<!--    <div class="btns">-->
<!--      <span class="btn" @click="clickDownload"><el-icon size="3vw" color="Black"><Download /></el-icon></span>-->
<!--      <span class="btn" @click="clickShare"><el-icon size="3vw" color="Black"><Share /></el-icon></span>-->
<!--      <span class="btn" @click="clickChange"><el-icon size="3vw" color="Black"><Refresh /></el-icon></span>-->
<!--    </div>-->

  </div>
</template>

<style scoped>
.pic {
  background-color: #e0ceb4;
  width: 50%;
  height: 100%;
  padding: 1vw;
}

.detail {
  background-color: #e0ceb4;
  width: 50%;
  height: 100%;
  padding: 0.5vw;
}

.name {
  margin-top: 3vh;
  font-size: 2vw;
  font-weight: normal;
  color: #992e22;
  margin-left: 1vw;
}

.rate {
  margin-top: 0.5vh;
  margin-left: 2.5vw;
  color: black;
}

h2 {
  margin-left: 0.3vw;
  font-size: 2vw;
  font-weight: normal;
}

.description {
  margin-top: 1vh;
  margin-left: 3vw;
  width: 30vw;
  font-size: medium;
  color: black;
}

h1 {
  font-size: 3vw;
}

.btns {
  width: 15vw;
  height: 5vh;
  position: absolute;
  right: 1vw;
  bottom: 5vh;
}

.btn {
  height: 5vw;
  width: 3vw;
  margin-right: 1.5vw;
}
</style>