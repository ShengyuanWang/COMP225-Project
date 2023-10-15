<script setup>

import Menu from "../../components/Menu.vue";
import {getCurrentInstance} from "vue";
import DrinkItem from "@/components/DrinkItem.vue";
import {tabNavEmits} from "element-plus";
const { proxy } = getCurrentInstance()
const res = {}
const getData = () => {
  var api="https://comp-225-project-backend.vercel.app/test/";
  //2.使用axios 进行get请求
  proxy.axios.get(api).then((res)=>{
    //请求成功的回调函数
    console.log(res)
    console.log(api)
  }).catch((err)=>{
    //请求失败的回调函数
    console.log(err)
  })
}
getData()
console.log(res)

const drinks = [
    {
      name: 'whiskey',
      instruction: 'whiskey-instruction'
    },{
    name: 'burbon',
    instruction: 'burbon-instruction'
  },{
    name: 'whiskey1',
    instruction: 'whiskey1-instruction'
  },{
    name: 'whiskey3',
    instruction: 'whiskey-instruction'
  },{
    name: 'burbon4',
    instruction: 'burbon-instruction'
  },{
    name: 'whiskey5',
    instruction: 'whiskey1-instruction'
  },
];


</script>

<template>

<perfect-scrollbar class="show">
  <div class="drink-table" >
    <drink-item v-for="drink in drinks" :name="drink.name" :instruction="drink.instruction">{{drink.name}}}</drink-item>
  </div>
</perfect-scrollbar>

</template>

<style scoped>
.show {
  width: 1730px;
  height: 100%;
  padding-left: 100px;
  padding-top: 60px;
}
.drink-table {
  width: 1600px;
  height: 100%;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 30px;
  padding-top: 10px;
}

</style>