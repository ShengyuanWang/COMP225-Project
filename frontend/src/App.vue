<script>
export default {
  methods: {
    toggleFullscreen() {
      let element = document.querySelector('.fullscreen');
      if (document.fullscreenElement) {
        document.exitFullscreen();
      } else {
        element.requestFullscreen();
      }
    }
  }
}
</script>

<template>
<div class="fullscreen">
  <router-view></router-view>
  <button @click="toggleFullscreen">Full Screen</button>
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
  z-index: 9999;
}

</style>
