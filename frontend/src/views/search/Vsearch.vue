<template>

  <div class="search">
    <Qinput></Qinput>
  </div>



</template>

<script>
import Qinput from "../../components/Qinput.vue";
import Menu from "../../components/Menu.vue";

export default {
  name: "Vsearch",
  components: {Menu, Qinput}
}
</script>

<style scoped>

.search {
  display: flex;
  position: relative;
}
</style>
