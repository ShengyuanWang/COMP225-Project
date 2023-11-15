<script setup>
// default import from firebase
import { storage } from '/src/firebase.js'
import { ref as storageRef, getMetadata, getDownloadURL } from "firebase/storage";
// packages from vue
import { ref } from 'vue';

// send property to father components
const props = defineProps({
  liquid: String, // the instruction about how to make the drink
  pos: String
})

// non-static variables
const liquid = storageRef(storage, 'images/'+ props.liquid+'.png'); // the firebase url
const liquid_url = ref(''); // the ture image access url

// functions
onload = () => {
  // function running on load
  loadImage();
}

const loadImage = () => {
  // load image according to liquid name
  getDownloadURL(liquid)
    .then((metadata) => {
      liquid_url.value = metadata;
    })
    .catch((error) => {
      console.log('error occured for loadImage');
    });
}
</script>

<template>
  <div class="txt">
    <el-image style="width: 15vw; position: fixed" :src="liquid_url" fit="fill" alt="Alcohol Image Onload"/>
  </div>
</template>

<style>
.txt {
  margin: 6vw;
  color: black;
  height: 20vh;
  width: 20vw;
}
</style>