<script setup>
// set up the props for passing in variables
import DrinkPic from "@/components/DrinkPic.vue";

const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  rating: Number, // the rating for the matching drink
  ingredients: Array, // the instructions for how to make the drink
  instructions: String, // the description for the drink,
  genres: Array,
  image: String
})


</script>

<template>
  <!--  detailed drink starts here-->
    <div class="pic drinkImageContainer" style="text-align: left;">
<!--      <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>-->
      <DrinkPic :liquid="props.image" style="height: 100%;" class="drinkImage"></DrinkPic>
    </div>
    <div class="pic drinkInfo">
      <div class="name"><h1>{{ props.name }}</h1></div>
      <div style="font-size: 1vw;" class="description">
        <p> {{instructions}} </p>
      </div>
      <div v-if="ingredients.length > 1" style="font-size: 1vw;" class="description">
        <p> Ingredients: </p>
         <ul>
          <li v-for="item in props.ingredients.slice(0, 4)">{{ item }}</li>
        </ul>
      </div>
      <div style="font-size: 1vw;" class="description"> 
        <p> Related book genres: {{genres.join(", ") }}</p>
      </div>
    </div>
</template>

<style scoped>

/* mobile formatting */
@media screen and (max-width: 800px) {
  .drinkImageContainer {
    width:100% !important;
    height: auto !important;
  }

  .drinkImage{
    height:30vh !important;
  }

  .drinkInfo {
    width: 100% !important;
  }

  .drinkInfo .description {
    font-size: 2.5vw !important;
  }

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