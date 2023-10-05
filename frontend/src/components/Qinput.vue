<script setup>
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
const place = ref(400)
const select = ref('')
const input = ref('aaa')
// 400 default 35 active
const data = [
  {
    value:'cocktail'
  },
  {
    value:'wine'
  },
  {
    value:'beer'
  },
  {
    value:'spirits'
  }
]
const onClick  = () => {
  place.value = 35;
}
</script>

<template>
  <div class="inp" :style="{marginTop: place+'px'}">
    <div class="mt-4">
      <el-input
          v-model="input"
          placeholder="Please input"
          class="input-with-select"
          size="large"
      >
        <template #prepend>
          <el-select v-model="value" :data="data" size="large" style="width:120px;" @click="onClick">
            <el-option v-for="item in data" :value="item.value">
            </el-option>
          </el-select>
        </template>
        <template #append  >
          <el-button :icon="Search" size="large" type="primary" @click="onClick"/>
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

