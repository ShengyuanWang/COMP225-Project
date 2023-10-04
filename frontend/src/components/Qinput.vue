<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
const input = ref('')
const select = ref('')
const value = ref(200)
const data = [
  {
    value:'1'
  },
  {
    value:'2'
  }
]
</script>

<template>
  <div class="inp" :style="{marginTop: value+'px'}">
    <div class="mt-4">
      <el-input
          v-model="input"
          placeholder="Please input"
          class="input-with-select"
          size="large"
      >
        <template #prepend>
          <el-select v-model="value" :data="data" size="large" style="width:120px;">
            <el-option v-for="item in data" :value="item.value">
            </el-option>
          </el-select>
        </template>
        <template #append>
          <el-button :icon="Search" size="large"/>
        </template>
      </el-input>
    </div>
  </div>


</template>

<style scoped>
.inp {
  width: 800px;
  margin-top: 400px;
  margin-left: auto;
  margin-right: auto;
  height: 100px;
  z-index:2;
}
img {
  width: 60px;
}


</style>

