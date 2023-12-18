<script setup>

import {getCurrentInstance, ref, onBeforeMount} from "vue";
import { useRouter, useRoute } from 'vue-router'
import DrinkItem from "@/components/DrinkItem.vue";
const { proxy } = getCurrentInstance()
const router = useRouter()
const route = useRoute()
const show = ref(0)
const drinks = ref({})
const res = {}

// get the data from route url
const type = route.query.type;



const onLoad = () => {
  var api = "https://comp-225-project-backend.vercel.app/getAlcohol/" + type;
  console.log(api);
  proxy.axios.get(api).then((res)=>{
    //请求成功的回调函数
    drinks.value = res.data;
    show.value = 1;
  }).catch((err)=>{
    //请求失败的回调函数
    console.log(err);
  })
}

const getData = (drink) => {
  console.log(drink);
  var api="https://comp-225-project-backend.vercel.app/test/";
  //2.使用axios 进行get请求
  // proxy.axios.get(api).then((res)=>{
  //   //请求成功的回调函数
  //   console.log(res);
  //   console.log(api);
  // }).catch((err)=>{
  //   //请求失败的回调函数
  //   console.log(err);
  // })
  router.push({ path: 'detail', query: {name: drink.name, type: drink.type, key_genres:drink.key_genres, ingredients:drink.ingredients, instructions:drink.instructions, liquid:drink.image}});
}


onBeforeMount(()=>{
  onLoad();
})

</script>

<template>


  <div class="fullscreen">
    <Menu></Menu>
    <perfect-scrollbar class="show" v-if="show===1">
      <div class="drink-table" >
        <drink-item v-for="drink in drinks"
                    :name="drink.name" 
                    :ingredients="drink.ingredients"
                    :description="drink.description"
                    :instructions="drink.instructions"
                    :liquid="drink.image"
                    url="https://firebasestorage.googleapis.com/v0/b/comp225-810dc.appspot.com/o/images%2FredWine.png?alt=media&token=2af7d5ed-b1e1-4382-95fe-2cdcc62fa79e"
                    @click="getData(drink)"
        >{{drink.name}}}</drink-item>
        <br>
        <div style="width: 90%"></div>
      </div>
    </perfect-scrollbar>

  </div>
</template>

<style scoped>
/* mobile formatting */
@media screen and (max-width: 600px) {
  .drink-item {
    width: 80vw;
  }
}

/* ipad formatting */
@media screen and (max-width: 1200px) and  (min-width: 600px){
  .drink-item {
    width: 40vw;
  }
}
.show {
  width: 100%;
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