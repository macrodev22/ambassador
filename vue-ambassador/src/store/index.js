import { defineStore } from "pinia";

const useStore = defineStore('store', {
    state: () => {
        return {
            auth: {
            user: JSON.parse(localStorage.getItem('user')) || null,
        },
        isLoading: false,
    }
    },
    actions: {
        setLoading(status) {
            this.isLoading = status
        },
    }
})

export default useStore