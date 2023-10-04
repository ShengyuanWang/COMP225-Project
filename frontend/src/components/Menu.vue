<template>
  <div class="menu">
      <div @click="isCollapse = !isCollapse" class="menu_icon"></div>
    <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        @open="handleOpen"
        @close="handleClose"
        style="margin-left:14px; margin-top:5px;background-color: #C3BCB3; border:none;"
    >
      <el-sub-menu index="1" style="background-color: #C3BCB3;">
        <template #title>
          <el-icon ><location /></el-icon>
          <span>Navigator One</span>
        </template>
        <el-menu-item-group>
          <template #title><span>Group One</span></template>
          <el-menu-item index="1-1">item one</el-menu-item>
          <el-menu-item index="1-2">item two</el-menu-item>
        </el-menu-item-group>
        <el-menu-item-group title="Group Two">
          <el-menu-item index="1-3">item three</el-menu-item>
        </el-menu-item-group>
        <el-sub-menu index="1-4">
          <template #title><span>item four</span></template>
          <el-menu-item index="1-4-1">item one</el-menu-item>
        </el-sub-menu>
      </el-sub-menu>
      <el-menu-item index="2">
        <el-icon><icon-menu /></el-icon>
        <template #title>Navigator Two</template>
      </el-menu-item>
      <el-menu-item index="3" disabled>
        <el-icon><document /></el-icon>
        <template #title>Navigator Three</template>
      </el-menu-item>
      <el-menu-item index="4">
        <el-icon><setting /></el-icon>
        <template #title>Navigator Four</template>
      </el-menu-item>
    </el-menu>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import {
  Document,
  Menu as IconMenu,
  Location,
  Setting,
} from '@element-plus/icons-vue'

const isCollapse = ref(true)
const handleOpen = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
  console.log(isCollapse)
}
const handleClose = (key: string, keyPath: string[]) => {
  console.log(key, keyPath)
}
</script>

<style>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.menu {
  list-style-type: none;
  margin-top: 30px;
  padding: 0;
  height: 100%; /* 全屏高度 */
  position: fixed;
  overflow: auto; /* 如果导航栏选项多，允许滚动 */
  z-index: 1;
  overflow-x: hidden;
  background-color: #C3BCB3;
}
.menu_icon{
  width: 60px;
  height: 40px;
  border-top: 3px solid #000000;
  border-bottom: 3px solid #000000;
  padding: 15.5px 0;
  background-clip: content-box;
  background-color: #000000;
  margin-left: 15px;
  margin-top: 10px;
}


</style>