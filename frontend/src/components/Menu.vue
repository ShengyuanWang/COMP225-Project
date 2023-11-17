<script setup>
// import required packages
import { ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
const router = useRouter()
const route = useRoute()

// non-static variables
const showPreference = ref(false) // const for whether show the preference list
const isCollapse = ref(true) // const for side-menu collapse action
const w = ref(6) // handle the distance to the left for the icon vw
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
  if (w.value === 6) {
    w.value = 22
    menuColor.value = '#D8C3A5'
  } else {
    w.value = 6
    menuColor.value = '#C3BCB3'
  }
}

// function to handle click action for the preference
const setPreference = () => {
  showPreference.value = true
}


// function handle the action on click the menu icon
const clickMenu = (gene) => {
  console.log('Click Menu');
  console.log(route.fullPath);
  router.push({ path: 'show', query: {type: gene}});
  console.log(route.fullPath);
}

// function handle the click action for the search icon
const clickMatch = () => {
  console.log('Click Match')
  router.push({ path: 'search'})
}



</script>


<template>
  <div class="menu" :style="{width: w+ 'vw', backgroundColor:menuColor}">
      <button name='menu-bar' @click="handleCollapse" class="menu_icon" :style="{marginLeft:w-4.5+'vw',marginRight:'2vw',height:'4vh',width:'3vw'}"></button>
    <div v-if="!isCollapse && !showPreference">
      <h1 @click="clickMatch()">Menu</h1>
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo el-collapse"
          @open="handleOpen"
          @close="handleClose"
          :style="{marginLeft:'1vw', marginTop:'0.5vh', border:'none', backgroundColor:menuColor}"
      >
        <el-sub-menu index="1" @click="clickMenu('Cocktail')">
          <template #title>
            <a href="#">Cocktail</a>
          </template>
        </el-sub-menu>

        <el-sub-menu index="2" @click="clickMenu('Wine')">
          <template #title>
            <a href="#">Wine</a>
          </template>
        </el-sub-menu>
        <el-sub-menu index="3" @click="clickMenu('Beer')">
          <template #title>
            <a href="#">Beer</a>
          </template>
        </el-sub-menu>
        <el-sub-menu index="4" @click="clickMenu('Spirits')">
          <template #title>
            <a href="#">Spirits</a>
          </template>
        </el-sub-menu>
      </el-menu>
      <h1>Preference</h1>
      <div class="check">
        <p><el-checkbox v-model="preference.beer" label="Beer" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="preference.wine" label="Wine" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="preference.spirits" label="Spirits" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="preference.cocktails" label="Cocktails" size="large" style="color: black"/></p>
      </div>
      <h1>Allergies</h1>
      <div class="check">
        <p><el-checkbox v-model="allergy.treenuts" label="Tree Nuts" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="allergy.peanuts" label="Peanuts" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="allergy.soy" label="Soy" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="allergy.seasame" label="Seasame" size="large" style="color: black"/></p>
        <p><el-checkbox v-model="allergy.other" label="Other" size="large" style="color: black"/></p>
      </div>
    </div>
  </div>
</template>



<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 20.5vw;
  min-height: 40vh;
  background-color: #D8C3A5;
}

.el-collapse {
  background-color: #D8C3A5;
}

.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 20.5vw;
  min-height: 20vh;
  background-color: #D8C3A5;
}

.el-checkbox__label{
  height: 2.4vh;
  font-size: 1vw !important;
}

.el-checkbox__input.is-checked .el-checkbox__inner,
.el-checkbox__input.is-indeterminate .el-checkbox__inner {
  border-color: #6A1006 !important;
  background-color: #6A1006 !important;
}
.el-checkbox__input.is-checked+.el-checkbox__label{
  color: #6A1006 !important;
}
.el-checkbox__inner:hover{
  border-color: #6A1006 !important;
}
.el-checkbox__input.is-focus .el-checkbox__inner {
  border-color: #6A1006 !important;
}

.menu {
  list-style-type: none;
  padding: 0;
  height: 100%;
  position: fixed;
  overflow: auto;
  z-index: 1;
  overflow-x: hidden;
  background-color: #D8C3A5;
}

.menu_icon{
  height: 4vh;
  border-top: 0.3vh solid black;
  border-bottom: 0.3vh solid black;
  border-left: 0px;
  border-right: 0px;
  padding: 1.6vh 0;
  background-clip: content-box;
  background-color: black;
  margin-top: 1.8vh;
  //margin-left: 10px;
}


h1 {
  font-size: 2.5vw;
  margin-top: 0.5vh;
  margin-left: 1.7vw;
  color: #992e22;
}

h2 {
  font-size: 1.5vw;
  margin-left: 1.7vw;
  color: #992e22;
}

menu {
  padding-inline-start: 0.5vw;
}

.preference {
  color: white
}

a {
  color: black;
}

.check {
  margin-left: 2vw;
  font-size: 1.3vw;
  font-weight: bold;
}
</style>