

<script setup>
import { ref } from 'vue';
import {all} from "axios";
const allergies = ref({gluten: false,
  lactose: false,
  egg: false,
  treenuts: false,
  soy: false,
  shellfish: false,
  fish: false});
const types = ref({  Beer: true,
  Wine: true,
  Spirits: true,
  Cocktails: true});
// 父组件传递过来事件

const findTypes = ref('')
const findAllergies = ref('')

const childValFn = (e)=>{
  //接收子组件传递给父组件的值
  console.log(e)
  allergies.value = e.allergy.value;
  types.value = e.preference.value;
  let allergyList = [];
  for (const allergy in allergies.value) {
    if (allergies.value[allergy] === true) {
      allergyList.push(allergy)
    }
  }
  if (allergyList.length > 0) {
    findAllergies.value = allergyList.join(',')
  } else {
    findAllergies.value = 'Nan'
  }

  let typeList = [];
  for (const type in types.value) {
    if (types.value[type] === true) {
      typeList.push(type)
    }
  }
  if (typeList.length > 0) {
    findTypes.value = typeList.join(',')
  } else {
    findTypes.value = 'Nan'
  }

  console.log(findTypes, findAllergies)
}

const test = ()=> {
  console.log(findTypes)
  console.log(findAllergies)
}



</script>

<template>

  <div class="fullscreen">
    <Menu @childClick="childValFn"></Menu>
    <div class="search" @click="test">
      <!--      <Qinput move place="350" place-holder="Please type in the book name" :allergies=allergies :types=types></Qinput>-->
      <Qinput move place="350" place-holder="Please type in the book name" :find-allergies=findAllergies :find-types=findTypes></Qinput>

    </div>


  </div>
</template>

<style scoped>
.search {
  display: flex;
  position: relative;
}
</style>
