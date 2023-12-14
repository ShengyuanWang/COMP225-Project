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
    return `Published by ${name} in ${date}`;
  } else if (name != null && name != '') {
    return `Published by ${name}`;
  } else if (date != null && date != '' != null) {
    return `Published in ${date}`;
  } else {
    return ``;
  }
}


</script>

<template>
  <!--  detailed drink starts here-->
  <div v-show="showDrink" class="pic" id="drink-image" style="text-align: left;">
    <DrinkPic :liquid=drink.image :key="drink.image"></DrinkPic>
<!--    <el-image :src="props.url" fit="cover" alt="Alcohol Image Onload" style="width: 100%;height: 100%"/>-->
  </div>
  <div v-show="showDrink" className="pic">
    <div className="name"><h1> Pairing: {{ drink.name }}</h1></div>
    <div className="name" v-show="title != '' && authors.length > 0" ><h2> Book: {{ title }} by {{formatAuthors(authors)}}</h2></div>
    <div className="name" v-show="title != '' && authors.length <= 0" ><h2> Book: {{ title }}</h2></div>
    <div style="font-size: 1vw;" className="description">
      <p> {{ drink.instructions }} </p>
    </div>
    <div v-if="drink.ingredients && drink.ingredients.length > 1" style="font-size: 1vw;" className="description">
      <p> Ingredients: </p>
      <ul>
        <li v-for="item in drink.ingredients.slice(0, 4)">{{ item }}</li>
      </ul>
    </div>
    <div v-show=" drink.notes && drink.notes.length > 0" style="font-size: 1vw;" className="description">
<!--      <p> Related book genres: {{ genres.join(", ") }}</p>-->
      <p>Note: {{drink.notes}}</p>
    </div>
    <div className="description">
      <button @click="changePage">{{buttonName}}</button>
      <button @click="reroll">Reroll</button>
    </div>
  </div>
  <div v-show="!showDrink" className="pic" id="imageContainer">
    <el-image :src="coverLink" fit="cover" alt="Alcohol Image Onload" style="width: 60%;height: 60%;"/>
  </div>
  <div v-show="!showDrink" className="pic">
    <div className="name" v-show="title != ''"><h1>{{ title }}</h1></div>
    <div className="name" v-show="authors.length > 0"> <h2> By: {{formatAuthors(authors)}} </h2> </div>
    <div className="name"><h3> {{ formatPublicationInfo(publisher, publicationDate) }} </h3></div>
    <div style="font-size: 1vw;" className="description">
      {{ description }}
    </div>
    <div className="description">
      <button class="bookInfo" @click="changePage">{{buttonName}}</button>
    </div>
  </div>
</template>

<style scoped>

#imageContainer {
  display: flex;
  justify-content: center;
  align-items: center;
}

.description button {
  color: white;
  font-size: 2.3vh;
  background-color: #992e22;
  width: 15vw;
  height: 5vh;
  border: 1px solid white;
  border-radius: 3px;
  text-align: center;
  margin: 1vh;
  justify-items: center;
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
  font-size: 5vw;
}

h2 {
  font-size: 2vw;
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