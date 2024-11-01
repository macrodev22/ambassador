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

        <v-btn @click="handleReset">
            clear
        </v-btn>
    </form>
</template>
<script setup>
import { reactive } from 'vue';
import client from '@/services/axiosClient';

const productDetails = reactive({
    title: '', description: '', image: '', price: ''
})

const submit = async () => {
    const { data } = await client.post('/products', productDetails)
}
</script>