<script setup>
// import required packages
import { ref } from 'vue'
import router from "@/router";

const showPreference = ref(false) // const for whether show the preference list
const isCollapse = ref(true) // const for side-menu collapse action
const w = ref(100) // handle the distance to the left for the icon
const menuColor = ref('#C3BCB3') // handle the color for the menu
// array for drink preference | default : false
const preference  = ref({
  beer: false,
  wine: false,
  spirits: false,
  cocktails: false
})
// array for allergy preference | default : false
const allergy  = ref({
  treenuts: false,
  peanuts: false,
  soy: false,
  seasame: false,
  other: false
})

// function for handle the collapse action for the sub-menu
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
  console.log(isCollapse)
}

// function for handle the close action for the sub-menu
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}

// function for handle the close action for the menu
const handleCollapse = () =>{
  isCollapse.value = !isCollapse.value
  showPreference.value = false
  console.log(w);
  if (w.value == 100) {
    w.value = 400
    menuColor.value = '#636466'
  } else {
    w.value = 100
    menuColor.value = '#C3BCB3'
  }
}

// function to handle click action for the preference
const setPreference = () => {
  showPreference.value = true
}

// function handle the action on click the menu icon
const clickMenu = () => {
  console.log('Click Menu');
  router.push({ path: 'show'})
}

// function handle the click action for the search icon
const clickMatch = () => {
  console.log('Click Match')
  router.push({ path: 'search'})
}


</script>


<template>
  <div class="menu" :style="{width: w+ 'px', backgroundColor:menuColor}">
      <div @click="handleCollapse" class="menu_icon" :style="{marginLeft:w-90+'px',marginRight:'40px'}"></div>
    <div v-if="!isCollapse && !showPreference">
      <h1>Menu</h1>
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo el-collapse"
          @open="handleOpen"
          @close="handleClose"
          :style="{marginLeft:'14px', marginTop:'5px', border:'none', backgroundColor:menuColor}"
      >
        <el-sub-menu index="1" class="bg-c" @click="clickMenu">
          <template #title>
            <span>cocktail</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="2" class="bg-c" @click="clickMenu">
          <template #title>
            <span>wine</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="3" class="bg-c" @click="clickMenu">
          <template #title>
            <span>beer</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="4" class="bg-c" @click="clickMenu">
          <template #title>
            <span>spirits</span>
          </template>
        </el-sub-menu>
      </el-menu>
      <h2 @click="setPreference">Set Preference</h2>
      <h1>Match</h1>
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo el-collapse"
          @open="handleOpen"
          @close="handleClose"
          :style="{marginLeft:'14px', marginTop:'5px', border:'none', backgroundColor:menuColor}"
      >
        <el-sub-menu index="5" class="bg-c" @click="clickMatch">
          <template #title>
            <span>Books</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="6" class="bg-c" @click="clickMatch">
          <template #title>
            <span>Movies</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="7" class="bg-c" @click="clickMatch">
          <template #title>
            <span>TV Shows</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="8" class="bg-c" @click="clickMatch">
          <template #title>
            <span>Music</span>
          </template>
        </el-sub-menu>
      </el-menu>
    </div>
    <div v-if="!isCollapse && showPreference">
      <h1>Preference</h1>
      <div class="check">
        <p><el-checkbox v-model="preference.beer" label="Beer" size="large" style="color: white" text-color="#"/></p>
        <p><el-checkbox v-model="preference.wine" label="Wine" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="preference.spirits" label="Spirits" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="preference.cocktails" label="Cocktails" size="large" style="color: white"/></p>
      </div>
      <h1>Allergies</h1>
      <div class="check">
        <p><el-checkbox v-model="allergy.treenuts" label="Tree Nuts" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="allergy.peanuts" label="Peanuts" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="allergy.soy" label="Soy" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="allergy.seasame" label="Seasame" size="large" style="color: white"/></p>
        <p><el-checkbox v-model="allergy.other" label="Other" size="large" style="color: white"/></p>
      </div>
    </div>


  </div>
</template>



<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 350px;
  min-height: 400px;
  background-color: #636466;
}
.el-collapse {
  background-color: #636466;
}
.menu {
  list-style-type: none;
  padding: 0;
  height: 100%; /* 全屏高度 */
  position: fixed;
  overflow: auto; /* 如果导航栏选项多，允许滚动 */
  z-index: 1;
  overflow-x: hidden;
  background-color: #C3BCB3;
}
.menu_icon{
  height: 40px;
  border-top: 3px solid black;
  border-bottom: 3px solid black;
  padding: 15.5px 0;
  background-clip: content-box;
  background-color: black;
  margin-top: 30px;
  margin-left: 10px;
}
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 350px;
  min-height: 200px;
  background-color: #636466;
}
h1 {
  font-size: 40px;
  margin-top: 5px;
  margin-left: 30px;
}
h2 {
  font-size: 25px;
  margin-left: 30px;
}
.preference {
  color: white
}


.el-checkbox__label{
  height: 24px;
  font-size: 20px !important;
}

.check {
  margin-left: 30px;
}

</style>