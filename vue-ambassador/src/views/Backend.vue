<template>
    <Products :products="products" />
</template>
<script setup>
import Products from '../components/Products.vue';
import { ref, onMounted } from 'vue';
import client from '../services/client';

const products = ref([])

onMounted(async () => {
    const { data } = await client.get('/products/backend')

    products.value = data.data
})

</script>