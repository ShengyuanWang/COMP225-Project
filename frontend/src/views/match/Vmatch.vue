<script setup>
// import required packages
import Qinput from "@/components/Qinput.vue";
import MatchResult from "@/components/MatchResult.vue";
import { useRoute } from 'vue-router'
import { ref } from 'vue'
const route = useRoute()

// get the variables from route url
const stars = route.query.stars;
const name = route.query.name;
const description = route.query.description;
const showResult = ref(false)
const show = () => {
  setTimeout(()=> {
    showResult.value = true;
  }, 2000)
}
show()
</script>

<template>
  <div class="header">
    <Qinput place="40"></Qinput>
  </div>
  <div class="loading" v-show="!showResult">
    <h1>Loading...Please Wait</h1>
  </div>
  <div class="match_result" v-show="showResult">
    <MatchResult url="https://i.ibb.co/989gpGR/drink1.png" :name=name :rating=stars :description=description></MatchResult>
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
}
</style>