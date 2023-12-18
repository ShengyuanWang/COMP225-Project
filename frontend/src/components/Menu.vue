<script setup>
// import required packages
import { ref } from 'vue'
import { onMounted } from 'vue'; 
import { useRouter, useRoute } from 'vue-router'
const router = useRouter()
const route = useRoute()

const props = defineProps({
  clickable: Boolean
})



// non-static variables
const showPreference = ref(false) // const for whether show the preference list
const isCollapse = ref(true) // const for side-menu collapse action
const w = ref(6) // handle the distance to the left for the icon vw
const menuColor = ref('#000435') // handle the color for the menu

onMounted(() => {
    if(screen.width <= 800) {
      w.value = 10
      menuColor.value = '#C3BCB3'
    }
})

// array for drink preference | default : true
const preference  = ref({
  Beer: true,
  Wine: true,
  Spirits: true,
  Cocktails: true
})

// array for allergy preference | default : false
const allergy  = ref({
  gluten: false,
  lactose: false,
  egg: false,
  treenuts: false,
  soy: false,
  shellfish: false,
  fish: false
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
const handleCollapse = () => {
  isCollapse.value = !isCollapse.value
  showPreference.value = false

  if (screen.width >= 800) {
    if (w.value === 6 || w.value === 10) {
      w.value = 20
      menuColor.value = '#dba858'
    } else {
      w.value = 6
      menuColor.value = '#000435'
    }
  } else {
    if (w.value === 6 || w.value === 10) {
      w.value = 40
      menuColor.value = '#dba858'
    } else {
      w.value = 10
      menuColor.value = '#000435'
    }

    console.log(w);
    console.log(props.clickable)

  }
}

// function to handle click action for the preference
  const setPreference = () => {
    showPreference.value = true
  }


// function handle the action on click the menu icon
  const clickMenu = (gene) => {
    // console.log('Click Menu');
    // console.log(route.fullPath);
    router.push({path: 'show', query: {type: gene}});
    console.log(route.fullPath);
  }

// function handle the click action for the search icon
  const clickMatch = () => {
    console.log('Click Match')
    router.push({path: 'search'})
  }

  const goHome = () => {
    console.log('Go Home');
    router.push({path: 'search'})
  }

  const emits = defineEmits(['childClick'])
  const toEmit = () => {
    // 触发父组件事件childClick并携带参数
    console.log(preference.value)
    emits('childClick', {preference, allergy})
  }

  const computeMenuIconMargin = () => {
    if (screen.width <= 800) {
      return w.value - 6
    } else {
      return w.value - 4.5
    }
  }


</script>

<template>

  <div class="menu" :style="{width: w + 'vw', backgroundColor:menuColor}">
      <button name='menu-bar' @click="handleCollapse()" class="menu_icon" :style="{marginLeft:computeMenuIconMargin()+'vw'}"></button>
      <el-button class="hideMobile home" type="primary" :style="{marginLeft:w-5.5+'vw',marginRight:'2vw',width:'5vw', marginTop:'4vh', backgroundColor:'#8b3e35', color:'#00000'}" @click="goHome">Home</el-button>


    <div v-if="!isCollapse && !showPreference">
      <el-button class="hideDesktop mobileButton" type="primary" :style="{marginLeft:'2vw', marginBottom:'1vh', height:'4vh', backgroundColor:'#8b3e35', color:'#00000'}"  @click="goHome">Home</el-button>
      <h1 @click="clickMatch()">Menu</h1>
      <p class="menu_item" @click="clickMenu('Wine')"> Wine </p>
      <p class="menu_item" @click="clickMenu('Cocktail')"> Cocktail </p>
      <p class="menu_item" @click="clickMenu('Beer')"> Beer </p>
      <p class="menu_item" @click="clickMenu('Spirits')"> Spirits </p>

      <h1 class="small">Preferences</h1>
      <div class="check">
        <p><el-checkbox v-model="preference.Beer" label="Beer" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="preference.Wine" label="Wine" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="preference.Spirits" label="Spirits" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="preference.Cocktails" label="Cocktails" size="large" style="color: black" @click="toEmit"/></p>
      </div>
      <h1 class="small">Allergies</h1>
      <div class="check">
        <p><el-checkbox v-model="allergy.gluten" label="Gluten" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.lactose" label="Lactose" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.egg" label="Egg" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.treenut" label="Tree Nuts" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.soy" label="Soy" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.shellfish" label="Shellfish" size="large" style="color: black" @click="toEmit"/></p>
        <p><el-checkbox v-model="allergy.fish" label="Fish" size="large" style="color: black" @click="toEmit"/></p>
      </div>
      <el-button class="mobileButton" type="primary" :style="{marginLeft:'2vw', marginBottom:'1vh', height:'4vh', backgroundColor:'#801e18', color:'#00000'}"  @click="toEmit">Save</el-button>
    </div>
  </div>
</template>

<style>
@media screen and (max-width: 800px) {
  .menu {
    z-index: 10 !important;
  }

  h1 {
    font-size: 5vw !important;
  }
  a {
    font-size: 3vw !important;
  }

  .small {
    font-size: 3.5vw !important;
  }

  .menu_icon {
    display: flex;
    justify-content: center;
  }



  .el-checkbox__label {
    font-size: 2.5vw !important;
  }

  .el-sub-menu__icon-arrow  {
    margin-right: -10vw !important;
  }

  .hideMobile {
    visibility: hidden;
    width: 0 !important;
    margin: 0 !important;
  }

  .hideDesktop{
    visibility: visible !important;
  }
  .mobileButton{
    width:12vw !important;
  }
}

.mobileButton {
  width:5vw;
}

.mobileButton:hover {
  background-color: #7c3730;
}
.hideDesktop{
  visibility: hidden;
}

.hideMobile{
  height:4vh;
}

.el-sub-menu__title{
  padding-right: 0 !important;
  padding-left: 1vw !important;
  width: 100% !important;
}
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
  font-size: 1vw;
}

.el-sub-menu{
  width: 100%;
}

.home:hover {
  background-color: #7c3730;
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
  width: w +'vw';
  background-color: #000435;
}

.menu_icon{
  height: 4vh;
  border-top: 0.3vh solid white;
  border-bottom: 0.3vh solid white;
  border-left: 0px;
  border-right: 0px;
  padding: 1.6vh 0;
  background-clip: content-box;
  background-color: white;
  margin-top: 1.8vh;
  margin-right: 2vw;
  width: 3vw;
}

.menu_icon:hover {
  cursor: pointer;
}

.menu_item {

  padding: 5px 10px 5px 10px;
  margin-left: 20px;
  //width: 100px;
  color: black;
  border-radius: 5px;

}

.menu_item:hover{
  background-color: #8b3e35;
  border: 1px solid white;
  color: white;
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

h3 {
  font-size: 2.5vw;
  margin-top: 0.5vh;
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