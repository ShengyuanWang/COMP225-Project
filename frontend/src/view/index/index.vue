<script setup>

</script>

<template>
  <div>
    <div style="display: flex; justify-content: center; align-items: center; position: relative;">
      <div class="title">
        BOOK + WINE
      </div>
    </div>
    <div class="center">
      <img src="./img/logo.png" alt="Center Image">
    </div>
    <div class="pop-up">
      <p class="question"> Are you over 21 ?</p>
      <div class="center">
        <div class="btn"><el-button type="primary" size="large"><p>Yes</p></el-button></div>
        <div class="btn"><el-button type="primary" size="large"><p>No</p></el-button></div>
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
}

.question {
  font-size: 30px;
  text-align: center;
}

.btn {
  margin-right: 50px;
}


</style>