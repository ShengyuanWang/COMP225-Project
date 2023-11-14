<script setup>

import {getCurrentInstance, ref} from "vue";
import { useRouter } from 'vue-router'
import DrinkItem from "@/components/DrinkItem.vue";
const { proxy } = getCurrentInstance()
const router = useRouter()

const show = ref(0)
const drinks = ref({})
const res = {}

const onLoad = () => {
  var api = "https://comp-225-project-backend.vercel.app/getAlcohol";
  proxy.axios.get(api).then((res)=>{
    //请求成功的回调函数
    drinks.value = res.data.alcohols;
    show.value = 1;
    console.log(show);
    console.log(drinks.value);
  }).catch((err)=>{
    //请求失败的回调函数
    console.log(err)
  })
}

const getData = (drink) => {
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

  router.push({ path: 'detail', query: {name: drink.name, instruction:drink.instruction}});
}

onLoad()




</script>

<template>

<perfect-scrollbar class="show" v-if="show===1">


  <div class="drink-table" >
    <drink-item v-for="drink in drinks" :name="drink.name" :instruction="drink.instructions" url="https://firebasestorage.googleapis.com/v0/b/comp225-810dc.appspot.com/o/images%2FredWine.png?alt=media&token=2af7d5ed-b1e1-4382-95fe-2cdcc62fa79e" @click="getData(drink)">{{drink.name}}}</drink-item>
    <br>
    <block style="width: 90%">aaaa</block>
  </div>


</perfect-scrollbar>

</template>

<style scoped>
.show {
  width: 95vw;
  height: 100%;
  padding-left: 8vw;
  padding-top: 1vh;
}
.drink-table {
  width: 90vw;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 1vh;
  padding-top: 1vh;
}




</style>