import { defineStore } from "pinia";

const useStore = defineStore('store', {
    state: () => {
        return {
            auth: {
            user: JSON.parse(localStorage.getItem('user')) || null,
        },
    }
    }
})

export default useStore