<!-- page that shows match -->
<script setup>
// import required packages
import Qinput from "@/components/Qinput.vue";
import MatchResult from "@/components/MatchResult.vue";
import LoadAnimation from "@/components/LoadAnimation.vue";
import { useRoute } from 'vue-router'
import {onBeforeMount, onMounted, ref} from 'vue'

const route = useRoute()

// get the variables from route url
const stars = route.query.stars;
const name = route.query.name;
const instructions = route.query.instructions;
const notes = route.query.notes;
const ingredients = route.query.ingredients;
const showResult = ref(false)
const placeHolder = ref(route.query.book);
const input = route.query.input;
const coverLink = route.query.coverLink;
const title = route.query.title;
const authors = route.query.authors;
const bookDescription = route.query.bookDescription;
const publisher = route.query.publisher;
const publicationDate = route.query.publicationDate;
const image= route.query.image;

let reRoll = [];
for ( let r = 0; r < route.query.reRolls.length; r+=1) {
  reRoll.push(JSON.parse(route.query.reRolls[r]));
}
const show = () => {
  showResult.value = true
}

const allergies = ref({gluten: false,
  lactose: false,
  egg: false,
  treenuts: false,
  soy: false,
  shellfish: false,
  fish: false});
const types = ref({  Beer: true,
  Wine: true,
  Spirits: true,
  Cocktails: true});

onMounted(()=>{
  setTimeout(() => {
    show()
  }, 2000);
  // console.log('mounted');
})

console.log(route.query)

</script>

<template>

  <div class="fullscreen">
    <Menu></Menu>
    <div class="header">
      <Qinput move place="60" :place-holder="placeHolder" :loadSceen=false></Qinput>
    </div>
    <!-- <div class="loading" v-show="!showResult">
      <h1 style="padding-left: 20vw; padding-top: 20vh; font-size: 40px">Loading Result ....</h1>
    </div> -->
    <LoadAnimation v-show="!showResult"></LoadAnimation>
    <div class="match_result" v-show="showResult">
      <MatchResult url="https://i.ibb.co/989gpGR/drink1.png"
                   :name=name
                   :instructions=instructions
                   :ingredients=ingredients
                   :notes=notes
                   :coverLink=coverLink
                   :title=title
                   :authors=authors
                   :bookDescription=bookDescription
                   :publisher=publisher
                   :publicationDate=publicationDate
                   :reRoll=reRoll
                   :image=image
      >
      </MatchResult>
    </div>

  </div>
</template>

<style scoped>
.header {
  height: 6vh;
  width: 100%;
}

.match_result {
  width: 80vw;
  height: 85vh;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw;
}

.loading {
  width: 80vw;
  height: 85vh;
  display: flex;
  position: relative;
  flex-flow: wrap;
  padding-left: 2vw;
  padding-top: 1vh;
  margin-left: 11vw;
  text-align: center;

}
</style>