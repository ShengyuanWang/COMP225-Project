<script>
export default {
  methods: {
    // toggleFullscreen() {
    //   let element = document.querySelector('.fullscreen');
    //   if (document.fullscreenElement) {
    //     document.exitFullscreen();
    //   } else {
    //     element.requestFullscreen();
    //   }
    // }
  }
}
</script>

<template>
<div class="fullscreen">
  <Menu></Menu>
  <router-view></router-view>
</div>


</template>

<style scoped>
.fullscreen {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: #C3BCB3;
}

</style>
