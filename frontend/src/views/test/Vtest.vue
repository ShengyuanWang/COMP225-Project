<script setup>
import DrinkPic from "@/components/DrinkPic.vue";
import { useRoute } from 'vue-router'
import {ref} from "vue";
import Menu from "@/components/Menu.vue";
const route = useRoute();
const activeName = ref('1')
</script>

<template>
  <perfect-scrollbar class="fullscreen">
    <Menu clickable="true"></Menu>
    <div class="header">
      <h1>
        ABOUT US
      </h1>
    </div>
    <div class="about">
      <p>
        Read & Sip was built by Team Miracal for COMP 225. It matches books with 90+ different alcoholic beverages.
        We use a custom pairing algorithm and all drink images were specially designed for this site.
      </p>
    </div>
    <div class="header">
      <h1> FAQ </h1>
    </div>
    <div class="questions">
      <el-collapse v-model="activeName" accordion>
        <el-collapse-item title="How are books paired with drinks?" name="1">
          <p>
            Read & Sip uses a custom pairing algorithm. The algorithm utilizes the book’s genres to find the best pairing,
            and for tie-breaks analyzes the book’s description as well.
          </p>
        </el-collapse-item>
        <el-collapse-item title="What books can I get pairings for?" name="2">
          <p>
            You can get pairings for almost any book, however some pairings may be less accurate than others.
            Our pairing algorithm works best with fiction and creative & biographical non-fiction.
            Our algorithm doesn’t work as well for educational and informational non-fiction.
            We use google books API to search for books, so our algorithm cannot make accurate pairings for books that google books does not catalog.

          </p>

        </el-collapse-item>
        <el-collapse-item title="Why doesn’t my book show up when I search for it?" name="3">
          <p>
            There is a chance if the book is very obscure or self-published google books doesn’t catalog it.
            What is more likely, is that there could be a typo in your title. Google books, which we use to search for books,
            tries to correct typos but sometimes it gets things wrong. Check the spelling of your title and try searching again.
          </p>

        </el-collapse-item>
        <el-collapse-item title="Why is my pairing not very accurate?" name="4">
          <p>Our algorithm is less optimized for some book genres. In the case of more educational and informational non-fiction books,
            our algorithm is less accurate, while pairings for fiction and creative & biographical nonfiction are more accurate.
            Additionally, if there is not a lot of genre data available for a certain book, then its pairing will be less accurate for that reason.
            This most often happens for very old or very new books.</p>
        </el-collapse-item>
      </el-collapse>
    </div>

  </perfect-scrollbar>

</template>

<style>
.header {
  width: 100%;
  text-align: center;
  height: auto;
}
.header h1 {
  color: #4f2335;
  font-family: DMSerifText,serif;
  font-weight: bolder;
  font-size: 5vw;
}

.about {
  background-color: #d3aa65;
  width: 70%;
  height: auto;
  margin: auto;
  border-color: white;
  border-radius: 10px;
  padding: 1vw;
  font-size: 2vw;
  color: #000435;
  font-family: DMSerifText,serif;
}

.questions {
  width: 70% ;
  height: auto;
  margin: auto;
  padding: 5px;
  background-color: #d3aa65 !important;
  border-color: white;
  border-radius: 10px;
}

.questions p {
  font-size: 1.5vw !important;
  color: #000435;
}

.el-collapse-item__header {
  background-color: #d3aa65 !important;
  font-size: 2vw !important;
  font-family: DMSerifText,serif;
  font-weight: bolder !important;
}

.el-collapse-item__content {
  padding: 0 1.5vw 0 1.5vw;
  background-color: #d3aa65;
  color: white;
}
</style>