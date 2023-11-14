<script setup>
// import required packages
import Menu from "../../components/Menu.vue";
import {getCurrentInstance, ref} from "vue";
import { useRouter } from 'vue-router'
import DrinkItem from "@/components/DrinkItem.vue";
import {tabNavEmits} from "element-plus";
const { proxy } = getCurrentInstance()
const router = useRouter()

const show = ref(0)
const drinks = ref({})
const res = {}
// const drinks = [
//   {
//     name: "WHISKEY SMASH",
//     instruction:
//         [
//           '2 oz. bourbon whiskey',
//           '3/4 oz. simple syrup',
//           '1/4 lemon',
//           'mint leaves'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'SAZERAC',
//     instruction:
//         [
//           '2 oz. cognac',
//           '1 splash rye whiskey',
//           '5 dashes Peychaud’s bitters',
//           '1 sugar cube',
//           '1 splash absinthe',
//           'lemon peel'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'PAPER PLANE',
//     instruction:
//         [
//           '3/4 oz. bourbon whiskey',
//           '3/4 oz. Aperol',
//           '3/4 oz. Amaro Nonino Quintessentia',
//           '3/4 oz. lemon juice'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'LION\'S TAIL',
//     instruction:
//         [
//           '2 oz. bourbon whiskey',
//           '1/2 oz. allspice dram',
//           '1/2 oz. lime juice',
//           '1 tsp. simple syrup',
//           '2 dashes Angostura bitters',
//           'orange peel'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'AMERICAN TRILOGY',
//     instruction:
//         [
//           '1 oz. rye whiskey',
//           '1 oz. apple brandy',
//           '1/2 oz. Apple Spice',
//           '2 dashes orange bitters'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name:'FORBIDDEN SOUR',
//     instruction: [
//       '1 oz. bourbon whiskey',
//       '1 oz. pomegranate liqueur',
//       '1 oz. lemon juice',
//       '1/2 oz. simple syrup'
//     ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'GIMLET',
//     instruction:
//         [
//           '2 oz. gin',
//           '1/2 oz. lime juice',
//           '1/2 oz. simple syrup',
//           'lime wheel'
//         ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'GOLD RUSH',
//     instruction: [
//       '2 oz. bourbon whiskey',
//       '3/4 oz. honey simple syrup',
//       '3/4 oz. lemon juice'
//     ],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }, {
//     name: 'MAPLE LEAF',
//     instruction:[
//       '2 oz. bourbon whiskey',
//       '1/2 oz. lemon juice',
//       '1/2 oz. maple syrup',
//       'cinnamon stick'],
//     url: "https://i.ibb.co/989gpGR/drink1.png"
//   }
// ];

const onLoad = () => {
  var api = "http://127.0.0.1:5000/getAlcohol";
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