<script setup>
  // import packages required
  import router from "../../router";
  import { ElNotification } from 'element-plus'
  import {ref} from 'vue';
  // define objects
  const obj = ref({
    clickable: false
  })

  // function for handling click yes btn
  const onClickYes = () => {
    console.log("click yes");
    router.push('search');
    obj.clickable.value = true;
    return 0;
  }

  // function for handling click no btn
  const onClickNo = () => {
    console.log("click no");
    ElNotification({
      title: 'UnderAge',
      message: 'You can not use the website for the underage issue!',
      type: 'warning',
    })
    return 0;
  }




</script>

<template>

  <div class="fullscreen">

    <Menu :clickable="obj.clickable"></Menu>
    <div>
      <div style="display: flex; justify-content: center; align-items: center; position: relative;">
        <div class="title">
          <h1 style="font-size: min(7vw, 10vh); margin-left: 0">READ & SIP</h1>

        </div>
      </div>
      <div class="center">
        <img src="/src/assets/logo.png" alt="Group Logo">
      </div>
      <div class="pop-up">
        <h2 class="question"> Are you over 21 ?</h2>
        <div class="center" style="width: auto;">
          <div class="btn"><el-button type="primary" size="large" @click="onClickYes()"><p>Yes</p></el-button></div>
          <div class="btn"><el-button type="primary" size="large" @click="onClickNo()"><p>No</p></el-button></div>
        </div>
      </div>
    </div>

  </div>
</template>

<style>
@media screen and (max-width: 800px) {
 .indexContainer {
  margin-top: 10vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
 }

 .center img {
  width: min(40vw, 50vh) !important;
  height: min(40vw, 50vh) !important;
 }

 .indexContainer h2 {
  font-size: 3vw !important;
 }

 .indexContainer h1 {
  font-size: min(8vw, 11vh) !important;
  margin-right: 1vw !important;
}

}
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
  position: relative;
  margin: 2vh 3vw;
}

.center img {
  width: min(30vw, 40vh);
  height: min(30vw, 40vh);
}

.question {
  font-size: 2vw;
  text-align: center;
  color: black;
}

.btn {
  margin: 1vw 1vw 1vw 1vw;
}

.center .el-button {
  background-color: #992e22 !important;
  border-color: #992e22 !important;
}

.indexContainer h1 {
  font-size: min(7vw, 10vh);
}
</style>