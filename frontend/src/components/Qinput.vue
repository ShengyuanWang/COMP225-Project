<script setup>
// import the required packages
import { ref } from 'vue'
import { Search } from '@element-plus/icons-vue'
import router from "@/router";

// set the props for the search bar
const props = defineProps({
  move: Boolean, // whether it should move
  place: String // the place of the search bar
})
const place = ref(props.place)
const value = ref('Books')
const input = ref('')
// 400 default 35 active
const data = [
  {
    value:'Books'
  },
  {
    value:'Movies'
  },
  {
    value:'TV Shows'
  },
  {
    value:'Music'
  }
]
const onClick  = () => {
  if (props.move) {
    place.value = 60;
  }
  router.push({path:'match', query: {name: 'SAZERAC', url:'https://i.ibb.co/989gpGR/drink1.png', stars:'5'}})
}
console.log(outerHeight)
</script>

<template>
  <div class="inp" :style="{marginTop: place+'px'}">
    <div class="mt-4">
      <el-input
          v-model="input"
          placeholder="Please input the name of the book"
          class="input-with-select"
          size="large"
      >
        <template #prepend>
          <el-select v-model="value" :data="data" size="large" style="width:120px;">
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
  margin-left: auto;
  margin-right: auto;
  height: 100px;
  z-index:2;
}
img {
  width: 60px;
}


</style>

