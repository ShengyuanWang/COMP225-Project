import { reactive } from 'vue'
import { ref } from 'vue'

// Because we need preferences and allergies to be the same across all instances of 
// components, we keep track of them in the store.
// This also makes it easier for us to send them to backend when user does a search

export const store = reactive({
    preference : ref({
        Beer: true,
        Wine: true,
        Spirits: true,
        Cocktails: true
      }),
    allergy : ref({
        gluten: false,
        lactose: false,
        egg: false,
        treenuts: false,
        soy: false,
        shellfish: false,
        fish: false
      })  

})