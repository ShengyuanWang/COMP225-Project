<script setup>
// set up the props for passing in variables
import DrinkPic from "@/components/DrinkPic.vue";

const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  rating: Number, // the rating for the matching drink
  ingredients: Array, // the instructions for how to make the drink
  instructions: String, // the description for the drink,
  key_genres: Array,
  image: String
})

const formatIngredients = (ingredients, asList) => {
  if (asList) {
      if (typeof(ingredients) === 'string') {
      return [ingredients]
    } else {
      return ingredients
    }
  } else {
    if (typeof(ingredients) === 'string') {
      return ingredients
    } else {
      return ingredients.join(", ")
    }
  }
}

const formatGenres = (genres ) => {
    if (typeof(genres) === 'string') {
      return "Related book topic" + genres
    } else {
      return "Related book topics and keywords: " + genres.join(", ")
    }
}

</script>

<template>
  <!--  detailed drink starts here-->
    <div class="pic drinkImageContainer" style="text-align: left;">
<!--      <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>-->
      <DrinkPic :liquid="props.image" style="height: 100%;" class="drinkImage"></DrinkPic>
    </div>
    <div class="pic drinkInfo">
      <div class="name noPadding"><h1>{{ props.name }}</h1></div>
      <div class="noPadding description" style="font-size: 1vw;">
        <p> {{instructions}} </p>
      </div>
      <div v-if="ingredients.length > 1" style="font-size: 1vw;" class="description noPadding">
        <p v-show="ingredients.length > 5"> 
          Ingredients: {{ formatIngredients(props.ingredients, false) }}
        </p>
        <p v-show="ingredients.length <= 5"> Ingredients: </p>
         <ul v-show="ingredients.length <= 5">
          <li v-for="item in formatIngredients(props.ingredients, true)">{{ item }}</li>
        </ul>
      </div>
      <div style="font-size: 1vw;" class="description noPadding"> 
        <p v-show="key_genres.length > 0"> {{formatGenres(key_genres) }}</p>
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
    height:25vh !important;
  }

  .drinkInfo {
    width: 100% !important;
    height: auto;

  }

  .drinkInfo .description {
    font-size: 2vw !important;
    line-height: 2vh;
  }

}

.noPadding{
  margin-left: 0 !important;
  margin-right: 1vw;
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

.drinkInfo h1 {
  font-size: 5vw;
  line-height: 10vh;
  margin-left: 0 !important;
}

.drinkInfo h2 {
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