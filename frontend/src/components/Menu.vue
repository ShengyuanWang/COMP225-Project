<template>
  <div class="menu" :style="{width: w+ 'px', backgroundColor:menuColor}">
      <div @click="handleCollapse" class="menu_icon" :style="{marginLeft:w-90+'px',marginRight:'40px'}"></div>
    <div v-if="!isCollapse">
      <el-menu
          default-active="2"
          class="el-menu-vertical-demo el-collapse"
          @open="handleOpen"
          @close="handleClose"
          :style="{marginLeft:'14px', marginTop:'5px', border:'none', backgroundColor:menuColor}"
      >
        <el-sub-menu index="1" class="bg-c">
          <template #title>
            <el-icon><location /></el-icon>
            <span>cocktail</span>
          </template>
          <!--        <el-menu-item-group class="bg_c">-->
          <!--          <template #title><span>Group One</span></template>-->
          <!--          <el-menu-item index="1-1">item one</el-menu-item>-->
          <!--          <el-menu-item index="1-2">item two</el-menu-item>-->
          <!--        </el-menu-item-group>-->
          <!--        <el-menu-item-group class="bg_c">-->
          <!--          <template #title><span>Group Two</span></template>-->
          <!--          <el-menu-item index="2-1">item one</el-menu-item>-->
          <!--          <el-menu-item index="2-2">item two</el-menu-item>-->
          <!--        </el-menu-item-group>-->
        </el-sub-menu>
        <el-sub-menu index="2" class="bg-c">
          <template #title>
            <span>wine</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="3" class="bg-c">
          <template #title>
            <span>beer</span>
          </template>
        </el-sub-menu>
        <el-sub-menu index="4" class="bg-c">
          <template #title>
            <span>spirits</span>
          </template>
        </el-sub-menu>
      </el-menu>
    </div>



  </div>
</template>

<script setup>
import { ref } from 'vue'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

const isCollapse = ref(true)
const w = ref(100)
const menuColor = ref('#C3BCB3')
const handleOpen = (key, keyPath) => {
  console.log(key, keyPath)
  console.log(isCollapse)
}
const handleClose = (key, keyPath) => {
  console.log(key, keyPath)
}

const handleCollapse = () =>{
  isCollapse.value = !isCollapse.value
  console.log(w);
  if (w.value == 100) {
    w.value = 400
    menuColor.value = '#636466'
  } else {
    w.value = 100
    menuColor.value = '#C3BCB3'
  }
}


</script>

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


</style>