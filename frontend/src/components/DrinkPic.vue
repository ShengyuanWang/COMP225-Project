<!-- This component contains the picture of the drink -->
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
      console.log(liquid_url);
    })
    .catch((error) => {
      console.log('error occured for loadImage');
    });
}

onload()
</script>

<template>
  <div class="txt">
    <img :src="liquid_url" :key="liquid_url"  :alt="props.liquid" style="object-fit: scale-down"/>
  </div>
</template>

<style>
.txt {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;
}
</style>