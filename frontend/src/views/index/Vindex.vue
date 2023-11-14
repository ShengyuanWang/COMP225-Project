<script setup>
  // import packages required
  import router from "../../router";
  import {reactive} from "vue";

  // define objects
  const obj = reactive({
    underage: 0
  })

  // function for handling click yes btn
  const onClickYes = () => {
    console.log("click yes");
    router.push('search');
    return 0;
  }

  // function for handling click no btn
  const onClickNo = () => {
    console.log("click no");
    obj.underage = 1;
    return 0;
  }




</script>

<template>
  <div>
    <div style="display: flex; justify-content: center; align-items: center; position: relative;">
      <div class="title">
        <h1 style="font-size: 7vw" v-if="obj.underage">BOOK + JUICE</h1> <h1 style="font-size: 7vw" v-else>BOOK + WINE</h1>
      </div>
    </div>
    <div class="center">
      <img src="/src/assets/logo.png" alt="Group Logo">
    </div>
    <div class="pop-up">
      <h2 class="question"> Are you over 21 ?</h2>
      <div class="center">
        <div class="btn"><el-button type="primary" size="large" @click="onClickYes()"><p>Yes</p></el-button></div>
        <div class="btn"><el-button type="primary" size="large" @click="onClickNo()"><p>No</p></el-button></div>
      </div>
    </div>
  </div>
</template>

<style>
.title {
  color: #636466;
  font-size: 7vw;
  text-align: center;
  font-weight: bold;
  margin-top: 2vh;
  margin-bottom: 2vh;
  display: block;
}




.center {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
  //width: 20vw; /* Optional: Makes the container the full height of the viewport for vertical centering */
  position: relative;
  margin: 2vh 3vw;
}

.center img {
  width: 30vw;
}

.question {
  font-size: 2vw;
  text-align: center;
  color: black;
}

.btn {
  margin-right: 3vw;
}

.center .el-button {
  background-color: #992e22 !important;
  border-color: #992e22 !important;
}


</style>