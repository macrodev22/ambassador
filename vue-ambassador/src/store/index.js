import { defineStore } from "pinia";

const store = defineStore('store', {
    state: () => {
        return {
            auth: {
            user:null,
        },
    }
    }
})

export default store