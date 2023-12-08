<script setup>
import {ref} from "vue";
// set up the props for passing in variables
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  description: String, // the rating for the matching drink
  ingredients: Array, // the instructions for how to make the drink
  notes: String, // the description for the drink,
  coverLink: String,
  title:String,
  author:String

})

const showDrink = ref(true);

const buttonName = ref("Book");

const changePage = () => {
  if (buttonName.value == "Book") {
    buttonName.value = "Drink"
    showDrink.value = !showDrink.value;
  } else {
    buttonName.value = "Book"
    showDrink.value = !showDrink.value;

  }
  console.log("click")
}
</script>

<template>
  <!--  detailed drink starts here-->
  <div v-show="showDrink" className="pic">
    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>
  </div>
  <div v-show="showDrink" className="pic">
    <div className="name"><h1>{{ props.name }}</h1></div>
    <div style="font-size: 1vw;" className="description">
      <p> {{ props.description }} </p>
    </div>
    <div v-if="props.ingredients.length > 1" style="font-size: 1vw;" className="description">
      <p> Ingredients: </p>
      <ul>
        <li v-for="item in props.ingredients.slice(0, 4)">{{ item }}</li>
      </ul>
    </div>
    <div v-show="notes.length > 0" style="font-size: 1vw;" className="description">
<!--      <p> Related book genres: {{ genres.join(", ") }}</p>-->
      <p>Notes: {{notes}}</p>
    </div>
    <div className="description">
      <button @click="changePage">{{buttonName}}</button>

    </div>
  </div>
  <div v-show="!showDrink" className="pic">
    <el-image :src="coverLink" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>
  </div>
  <div v-show="!showDrink" className="pic">
    <div className="name"><h1>{{ title }}</h1></div>
    <div style="font-size: 1vw;" className="description">
      <p> {{ author }} </p>
    </div>

    <div className="description">
      <button @click="changePage">{{buttonName}}</button>
    </div>
  </div>
</template>

<style scoped>
.description button {
  color: white;
  background-color: #992e22;
  width: 5vw;
}
.pic {
  background-color: #e0ceb4;
  width: 50%;
  height: 100%;
  padding: 2vh;
  opacity: 0.9;
}

.name {
  margin-top: 1vh;
  font-size: 3vw;
  font-weight: normal;
  color: #992e22;
}

h1 {
  font-size: 5vw;
}

h2 {
  font-size: 2vw;
  font-weight: normal;
}

.description {
  margin-left: 2vw;
  margin-top: 2vh;
  font-size: 1vw;
  color: black;
}
</style>