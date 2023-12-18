
<!-- search / home  page  -->
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
      <Qinput move place="350" place-holder="Enter book title" :loadScreen=true></Qinput>

    </div>


  </div>
</template>

<style scoped>
.search {
  display: flex;
  position: relative;
}
</style>
