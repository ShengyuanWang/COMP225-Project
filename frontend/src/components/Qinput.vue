<script setup>
// import the required packages
import {getCurrentInstance, ref} from 'vue'
import { Search } from '@element-plus/icons-vue'
import router from "@/router";
const {proxy} = getCurrentInstance()

// set the props for the search bar
const props = defineProps({
  move: Boolean, // whether it should move
  place: String, // the place of the search bar
  placeHolder: String, // the Place holder
  input: String
})
const place = ref(props.place)  // placeholder
const value = ref('Books')
const input = ref(props.input)
const placeHolder = ref(props.placeHolder)
// 400 default 35 active
const data = [
  {
    value:'Books'
  }
]


// functions
const onClick  = () => {
  if (props.move) {
    place.value = 60;
  }
  var api="https://comp-225-project-backend.vercel.app/test/" + input.value;
  // use axios to get
  proxy.axios.get(api).then((res)=>{
    console.log(api)
    console.log('finish')
    console.log(res)
    console.log("notes:")
    console.log(res.data.notes)
    router.push({path:'match', query: {name:res.data.name, url:'https://i.ibb.co/989gpGR/drink1.png', stars:'5', description:res.data.instructions, ingredients:res.data.ingredients, notes:res.data.notes, book:input.value, input:input.value}})
  }).catch((err)=>{
    console.log(err)
  })
}
</script>

<template>
  <div class="inp" :style="{marginTop: place+'px'}">
    <div class="mt-4">
      <el-input
          v-model="input"
          :placeholder="placeHolder"
          class="input-with-select"
          size="large"
          @keyup.enter="onClick"
      >
        <template #prepend>
          <p>BOOK</p>
<!--          <el-select v-model="value" :data="data" size="large" style="width:120px;">-->
<!--            <el-option v-for="item in data" :value="item.value">-->
<!--            </el-option>-->
<!--          </el-select>-->
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
  width: 50vw;
  margin-left: auto;
  margin-right: auto;
  height: 10vh;
  z-index:2;
}

img {
  width: 3.5vw;
}
</style>

