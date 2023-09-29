<script setup>
import { ref } from 'vue'
const input = ref('')
</script>

<template>
  <div class="inp">
    <el-input
        v-model="input"
        clearable
        placeholder="Enter book title here..."
    />
  </div>

</template>

<style scoped>
.inp {
  width: 60%;
  margin-top: 30%;
  margin-left: auto;
  margin-right: auto;
}
</style>

