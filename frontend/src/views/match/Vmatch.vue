<script setup>
// import required packages
import Qinput from "@/components/Qinput.vue";
import MatchResult from "@/components/MatchResult.vue";
import { useRoute } from 'vue-router'
import {onBeforeMount, onMounted, ref} from 'vue'

const route = useRoute()

// get the variables from route url
const stars = route.query.stars;
const name = route.query.name;
const description = route.query.description;
const notes = route.query.notes;
const ingredients = route.query.ingredients;
const showResult = ref(false)
const placeHolder = route.query.book;
const input = route.query.input;
const coverLink = route.query.coverLink;
const title = route.query.title;
const author = route.query.author;
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
// 父组件传递过来事件

const findTypes = ref('')
const findAllergies = ref('')

const childValFn = (e)=>{
  //接收子组件传递给父组件的值
  console.log(e)
  allergies.value = e.allergy.value;
  types.value = e.preference.value;
  let allergyList = [];
  for (const allergy in allergies.value) {
    if (allergies.value[allergy] === true) {
      allergyList.push(allergy)
    }
  }
  if (allergyList.length > 0) {
    findAllergies.value = allergyList.join(',')
  } else {
    findAllergies.value = 'Nan'
  }

  let typeList = [];
  for (const type in types.value) {
    if (types.value[type] === true) {
      typeList.push(type)
    }
  }
  if (typeList.length > 0) {
    findTypes.value = typeList.join(',')
  } else {
    findTypes.value = 'Nan'
  }

  console.log(findTypes, findAllergies)
}

onMounted(()=>{
  setTimeout(() => {
    show()
  }, 2000);
  console.log('mounted');
})



</script>

<template>


  <div class="fullscreen">
    <Menu @childClick="childValFn"></Menu>
    <div class="header">
      <Qinput move place="60" place-holder="Please type in the book name" :find-allergies=findAllergies :find-types=findTypes></Qinput>
    </div>
    <div class="loading" v-show="!showResult">
      <h1 style="padding-left: 20vw; padding-top: 20vh; font-size: 40px">Loading Result ....</h1>
    </div>
    <div class="match_result" v-show="showResult">
      <MatchResult url="https://i.ibb.co/989gpGR/drink1.png"
                   :name=name
                   :rating=stars
                   :description=description
                   :ingredients=ingredients
                   :notes=notes
                   :coverLink=coverLink
                   :title=title
                   :author=author
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