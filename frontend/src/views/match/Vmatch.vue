<script setup>
// import required packages
import Qinput from "@/components/Qinput.vue";
import MatchResult from "@/components/MatchResult.vue";
import { useRoute } from 'vue-router'
import {onBeforeMount, onMounted, ref} from 'vue'

const route = useRoute()

// get the variables from route url
const stars = route.query.stars;
const name = route.query.name;
const description = route.query.description;
const notes = route.query.notes;
const ingredients = route.query.ingredients;
const showResult = ref(false)
const placeHolder = route.query.book;
const input = route.query.input;
const show = () => {
  showResult.value = true

}

onMounted(()=>{
  setTimeout(() => {
    show()
  }, 2000);
  console.log('mounted');
})



</script>

<template>


  <div class="fullscreen">
    <Menu></Menu>
    <div class="header">
      <Qinput place="40" :place-holder="placeHolder" :input="input"></Qinput>
    </div>
    <div class="loading" v-show="!showResult">
      <h1 style="padding-left: 20vw; padding-top: 20vh; font-size: 40px">Loading Result ....</h1>
    </div>
    <div class="match_result" v-show="showResult">
      <MatchResult url="https://i.ibb.co/989gpGR/drink1.png"
                   :name=name
                   :rating=stars
                   :description=description
                   :ingredients=ingredients
                   :notes=notes>
      </MatchResult>
    </div>

  </div>
</template>

<style scoped>
.header {
  height: 6vh;
  width: 100%;
}

.match_result {
  width: 80vw;
  height: 85vh;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw;
}

.loading {
  width: 80vw;
  height: 85vh;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw;
  text-align: center;

}
</style>