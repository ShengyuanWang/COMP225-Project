import { reactive } from 'vue'
import { ref } from 'vue'

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