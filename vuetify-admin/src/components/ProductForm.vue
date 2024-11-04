<template>
    <form @submit.prevent="submit" class="mt-4">
        <v-text-field :counter="200" v-model="productDetails.title"
            label="Title"></v-text-field>

        <v-textarea :counter="500" v-model="productDetails.description"
            label="Description"></v-textarea>

        <v-text-field v-model="productDetails.image"
            label="Image"></v-text-field>

        <v-text-field type="number" v-model="productDetails.price"
            label="Price"></v-text-field>

        <v-checkbox   label="Option"
            type="checkbox" value="1"></v-checkbox>

        <v-btn class="me-4" type="submit">
            save
        </v-btn>

        <v-btn @click="clear">
            clear
        </v-btn>
    </form>
</template>
<script setup>
import { reactive, onMounted } from 'vue';
import client from '@/services/axiosClient';
import { useRoute, useRouter } from 'vue-router';

const route = useRoute()
const router = useRouter()

const productDetails = reactive({
    title: '', description: '', image: '', price: ''
})

const clear = () => {
    productDetails.description = ''
    productDetails.title = ''
    productDetails.image = ''
    productDetails.price = ''
}

const submit = async () => {
    // Creating a product
    if (!route.params.id) {
        const { data } = await client.post('/products', productDetails)
    } 
    // Editing a product
    else {
        const { data } = await client.put(`/products/${route.params.id}`, productDetails)
    }

    await router.push('/products')
}

onMounted(async () => {
    // Editing product
    if (route.params.id) {
        const id = route.params.id
        const { data } = await client.get(`/products/${id}`)
        productDetails.title = data.title
        productDetails.description = data.description
        productDetails.price = data.price
        productDetails.image = data.image
    }
})

</script>