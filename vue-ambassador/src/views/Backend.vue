<template>
    <Products :products="products" @set-search-filter="updateSearchFilter" />
</template>
<script setup>
import Products from '../components/Products.vue';
import { ref, onMounted, reactive, watch } from 'vue';
import client from '../services/client';

const products = ref([])
const filters = reactive({s: ''})

const loadProducts = async () => {
    const { data } = await client.get(`/products/backend?s=${filters.s}`)

    products.value = data.data
} 
onMounted(loadProducts)

const updateSearchFilter = (newQuery) => {
 filters.s = newQuery
}

watch(filters, loadProducts)

</script>