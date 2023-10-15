<script setup>

import Qinput from "@/components/Qinput.vue";
import MatchResult from "@/components/MatchResult.vue";
</script>

<template>
  <div class="header">
    <Qinput place="40"></Qinput>
  </div>
  <div class="match_result">
    <MatchResult url="https://i.ibb.co/989gpGR/drink1.png"></MatchResult>
  </div>

</template>

<style scoped>
.header {
  height: 60px;
  width: 100%;
}
.match_result {
  width: 1450px;
  height: 850px;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 30px;
  padding-top: 10px;
  background-color: blue;
  margin-left: 150px;
}
</style>