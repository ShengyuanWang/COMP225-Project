<script>
  import router from "../../router";
  import {reactive} from "vue";

  export default {
    setup() {
      const obj = reactive({
        underage: 0
      })
      function onClickYes() {
        console.log("click yes");
        router.push('search');
        return 0;
      }

      function onClickNo() {
        console.log("click no");
        obj.underage = 1;
        return 0;
      }
      return {
        obj,
        onClickYes,
        onClickNo
      }
    },
  }



</script>

<template>
  <div>
    <div style="display: flex; justify-content: center; align-items: center; position: relative;">
      <div class="title">
        <p v-if="obj.underage">BOOK + JUICE</p> <p v-else>BOOK + WINE</p>
      </div>
    </div>
    <div class="center">
      <img src="/src/assets/logo.png" alt="Center Image">
    </div>
    <div class="pop-up">
      <p class="question"> Are you over 21 ?</p>
      <div class="center">
        <div class="btn"><el-button type="primary" size="large" @click="onClickYes()"><p>Yes</p></el-button></div>
        <div class="btn"><el-button type="primary" size="large" @click="onClickNo()"><p>No</p></el-button></div>
      </div>
    </div>
  </div>
</template>

<style scss>
.title {
  color: #636466;
  font-size: 100px;
  text-align: center;
  font-weight: bold;
  margin-top: 20px;
  margin-bottom: 20px;
  display: block;
}

.center {
  display: flex;
  justify-content: center; /* Center horizontally */
  align-items: center; /* Center vertically */
//height: 200px; /* Optional: Makes the container the full height of the viewport for vertical centering */
  position: relative;
  margin-left: 40px;
  margin-right: 40px;
  margin-bottom: 20px;
}

.question {
  font-size: 30px;
  text-align: center;
  color: black;
}

.btn {
  margin-right: 50px;
}


</style>