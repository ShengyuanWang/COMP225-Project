<script setup>
import {ref} from "vue";
import DrinkPic from "@/components/DrinkPic.vue";
// set up the props for passing in variables
const props = defineProps({
  url: String, // the url for the image
  name: String, // the name of the drink
  instructions: String, // the rating for the matching drink
  ingredients: Array, // the instructions for how to make the drink
  notes: String, // the description for the drink,
  coverLink: String,
  title:String,
  authors:Array,
  publicationDate:String,
  publisher:String,
  bookDescription:String,
  reRoll: Array,
  image: String
})

const drink = ref({
  ingredients: props.ingredients,
  instructions: props.instructions,
  name: props.name,
  notes: props.notes,
  image: props.image
});

// console.log(props)

const reRollCnt = ref(1);

const showDrink = ref(true);

const buttonName = ref("Book Information");

const changePage = () => {
  if (buttonName.value === "Book Information") {
    buttonName.value = "Pairing Information"
    showDrink.value = !showDrink.value;
  } else {
    buttonName.value = "Book Information"
    showDrink.value = !showDrink.value;

  }
  // console.log("click")
}

const reroll = () => {
  console.log("click ReRoll")
  drink.value = props.reRoll[reRollCnt.value];
  reRollCnt.value = (reRollCnt.value + 1) % props.reRoll.length
  console.log(drink.value)
  if (drink.value.image === 'TBA') {
    drink.value.image = 'negroni'
  }
}

const formatAuthors = (authors_list) => {
  const author_count = authors_list.length;
  if (typeof(authors_list) == 'string') {
    return `${authors_list}`; 
  } else {
    if (author_count == 1) {
      return `${authors_list[0]}`;
    } else if (author_count == 2) {
      return `${authors_list[0]} and ${authors_list[1]}`;
    }  else if (author_count > 2) {
      return `${authors_list[0]} et al.`;
    } else {
      return '';  
  }
  }
}

const formatPublicationInfo = (name, date) => {
  if (name != null && name != '' && date != null && date != '') {
    const [year] = date.split("-");
    return `Published by ${name} in ${year}`;
  } else if (name != null && name != '') {
    return `Published by ${name}`;
  } else if (date != null && date != '') {
    const [year] = date.split("-");
    return `Published in ${year}`;
  } else {
    return ``;
  }
}

const trimDescription = (text) => {
  const maxLength = 800;
  if (text.length <= maxLength) {
    return text;
  } else {
    const textSubString = text.substring(0, maxLength);
    const lastPeriod = textSubString.lastIndexOf(' ');
    if (lastPeriod !== -1) {
      return '"' + textSubString.substring(0, lastPeriod) + '..."';
    } else {
      return '"' + textSubString + '..."';
    }
  }
}

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


</script>

<template>
  <!--  detailed drink starts here-->
  <div v-show="showDrink" class="pic pairingImageContainer" id="drink-image" style="text-align: left;">
    <DrinkPic :liquid=drink.image :key="drink.image" class="pairingImage"></DrinkPic>
<!--    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>-->
  </div>
  <div v-show="showDrink" className="pic pairingInfo">
    <div className="name"><h1> Pairing: {{ drink.name }}</h1></div>
    <div className="name" v-show="title != '' && authors.length > 0" ><h2> Book: {{ title }} by {{formatAuthors(authors)}}</h2></div>
    <div className="name" v-show="title != '' && authors.length <= 0" ><h2> Book: {{ title }}</h2></div>
    <div style="font-size: 1vw;" className="description">
      <p> {{ drink.instructions }} </p>
    </div>
    <div v-if="drink.ingredients  && drink.ingredients.length > 1" style="font-size: 1vw;" className="description">
      <p v-show="ingredients.length > 5"> 
          Ingredients: {{ formatIngredients(props.ingredients, false) }}
        </p>
      <p v-show="ingredients.length <= 5"> Ingredients: </p>
      <ul v-show="ingredients.length <= 5">
        <li v-for="item in formatIngredients(drink.ingredients, true)">{{ item }}</li>
      </ul>
    </div>
    <div v-show=" drink.notes && drink.notes.length > 0" style="font-size: 1vw;" className="description">
<!--      <p> Related book genres: {{ genres.join(", ") }}</p>-->
      <p>Note: {{drink.notes}}</p>
    </div>
    <div className="description buttonContainer">
      <button @click="changePage">{{buttonName}}</button>
      <button @click="reroll">Reroll</button>
    </div>
  </div>
  <div v-show="!showDrink && coverLink != ''" className="pic imageContainer">
    <el-image  :src="coverLink" fit="contain" alt="Alcohol Image Onload" style="width: 60%;height: 60%;"/>
  </div>
  <div v-show="!showDrink" className="pic bookInfo" :style="{ width: coverLink == '' ? '100%' : '50%', textAlign: title === '' ? 'center' : 'auto' }">
    <div className="name" v-show="title === ''"> <h2> We couldn't find information on your book. </h2></div>
    <div className="name" v-show="title != ''"><h1>{{ title }}</h1></div>
    <div className="name" v-show="authors.length > 0"> <h2> By {{formatAuthors(authors)}} </h2> </div>
    <div className="name"><h3> {{ formatPublicationInfo(publisher, publicationDate) }} </h3></div>
    <div style="font-size: 1vw;" className="description">
      {{ trimDescription(bookDescription) }}
    </div>
    <div className="description">
      <button class="bookInfo" @click="changePage">{{buttonName}}</button>
    </div>
  </div>
</template>

<style scoped>
@media screen and (max-width: 800px) {
  h1 {
    font-size: 6vw !important;
    line-height: 6vw !important;
  }

  h2 {
    font-size: 3vw !important;
  }

  h3 {
    font-size: 2.5vw !important;
  }

  .description {
    font-size: 2vw !important;
    margin-bottom: .6vh;
  }

  .buttonContainer {
    margin-top: -1vw !important;
  }

  .description button  {
    width: 30vw !important;
  }
  .pairingImageContainer {
    width:100% !important;
    height: auto !important;
  }

  .pairingImage{
      height:30vh !important;
    }

  .pairingInfo {
    width:100% !important;
  }

  .imageContainer {
    width:100% !important;
    height: auto !important;
  }

  .imageContainer .el-image {
    height: 25vh !important;
  }

  .bookInfo{
    width: 100% !important;
  }

}

.imageContainer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.buttonContainer {
  display: flex;
  justify-content: space-between;
}

.description button {
  color: white;
  font-size: 2.3vh;
  background-color: #992e22;
  width: 15vw;
  height: 6vh;
  border: 1px solid white;
  border-radius: 3px;
  text-align: center;
  margin: 1vh;
  justify-items: center;
}

.buttonContainer {
  margin: 0;
}
.bookInfo {
  margin: 0 !important;
}

.description button:hover {
  background-color: #87271d;
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
  font-size: 1vw;
  font-weight: normal;
  color: #992e22;
}

h1 {
  font-size: 3vw;
  line-height: 5vw;
}

h2 {
  font-size: 1.7vw;
  font-weight: normal;
}

h3 {
  font-size: 1.5vw;
  font-weight: normal;
}

.description {
  margin-left: 2vw;
  margin-top: 2vh;
  font-size: 1vw;
  color: black;
  position: flex;
  justify-content: space-between;
}
</style>