<script setup>
import { storage } from '/src/firebase.js'
import { ref as storageRef, getMetadata, getDownloadURL } from "firebase/storage";
import { ref } from 'vue';
const props = defineProps({
  liquid: String, // the instruction about how to make the drink
  pos: String
})
const imagesRef = storageRef(storage, 'images');
const liquid = storageRef(storage, 'images/'+ props.liquid+'.png');
const glass_url = ref('');
const liquid_url = ref('');
const finish = ref(0);

getDownloadURL(liquid)
    .then((metadata) => {
      // Metadata now contains the metadata for 'images/forest.jpg'
      console.log('success');
      liquid_url.value = metadata;
      finish.value = 1;
      console.log(liquid_url.value);
      console.log(finish);
    })
    .catch((error) => {
      // Uh-oh, an error occurred!
    });


</script>

<template>
  <div class="txt" v-if="finish===1">

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