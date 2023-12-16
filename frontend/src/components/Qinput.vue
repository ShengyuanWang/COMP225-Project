<script setup>
// import the required packages
import {getCurrentInstance, ref} from 'vue'
import { Search } from '@element-plus/icons-vue'
import router from "@/router";
const {proxy} = getCurrentInstance()

// set the props for the search bar
const props = defineProps({
  move: Boolean, // whether it should move
  place: String, // the place of the search bar
  placeHolder: String, // the Place holder
  input: String,
  findAllergies: String,
  findTypes: String
})

const place = ref(props.place)  // placeholder
const value = ref('Books')
const input = ref(props.input)
const placeHolder = ref(props.placeHolder)
const findTypes = ref(props.findTypes)
const findAllergies = ref(props.findAllergies)
// 400 default 35 active
const data = [
  {
    value:'Books'
  }
]





// functions
const onClick  = () => {

  if (props.move) {
    place.value = 60;
  }

  console.log('qinput')
  console.log(props)


    var api = "https://comp-225-project-backend.vercel.app/test/" + input.value + '/' + props.findTypes + '/' + props.findAllergies;
    // use axios to get
    proxy.axios.get(api).then((res) => {
      console.log(api)
      // console.log('finish')
      console.log(res)
      // console.log(res.data.rerolls)
      // console.log("notes:")
      // console.log(res.data)
      let reRolls = []
      for (let reroll in res.data.rerolls) {
        reRolls.push(JSON.stringify(res.data.rerolls[reroll]))
      }
      router.push({
        path: 'match',
        query: {
          name: res.data.name,
          url: 'https://i.ibb.co/989gpGR/drink1.png',
          stars: '5',
          instructions: res.data.instructions,
          ingredients: res.data.ingredients,
          description: res.data.description,
          notes: res.data.notes,
          book: input.value,
          input: input.value,
          coverLink: res.data.cover_link,
          title: res.data.title,
          authors: res.data.authors,
          bookDescription: res.data.bookDescription,
          publisher: res.data.publisher,
          publicationDate: res.data.publicationDate,
          reRolls: reRolls,
          image: res.data.image
        }
      })
    }).catch((err) => {
      console.log(err)
    })
  }
  
  const isMobile = () => {
    if(screen.width <= 800) {
      return true;
    } else {
      return false;
    }
  } 

</script>

<template>
  <div class="inp" :style="{marginTop: place+'px'}">
    <div class="mt-4">
      <el-input
          v-model="input"
          :placeholder="placeHolder"
          class="input-with-select"
          size="large"
          @keyup.enter="onClick"
      >
        <template v-if="!isMobile()" #prepend div="bookLabel">
          <p>BOOK</p>
        </template>
        <template #append  >
          <el-button :icon="Search" size="large" type="primary" @click="onClick(props)"/>
        </template>
      </el-input>
    </div>
  </div>
</template>

<style scoped>
@media screen and (max-width: 800px) {
  .inp { 
    width: 60vw !important;
  }
}
.inp {
  width: 50vw;
  margin-left: auto;
  margin-right: auto;
  height: 10vh;
  z-index:2;
}

img {
  width: 3.5vw;
}
</style>

