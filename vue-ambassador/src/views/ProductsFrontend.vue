<template>
    <Products :products="filteredProducts" @set-search-filter="updateFilters" />
</template>
<script setup>
import Products from '../components/Products.vue';
import { ref, onMounted, watch, reactive } from 'vue';
import client from '../services/client';

const products = ref([])
const filteredProducts = ref([])
const filters = reactive({})

const loadProducts = async () => {
    console.log('Loading products')
    const { data } = await client.get(`/products/frontend`)
    products.value = data
    return Promise.resolve()
}

const filterProducts = (filters) => {
    filteredProducts.value = products.value

    // Filter products
    if (filters.s) {
        // By search term
        let q = filters.s.toLowerCase()
        filteredProducts.value = products.value.filter((p) => {
            return p.title.toLowerCase().includes(q) || p.description.toLowerCase().includes(q)
        } )
    }
}

onMounted(async () => {
    await loadProducts()
    filteredProducts.value = products.value
})

const updateFilters = (newQuery) =>  {
    filters.s = newQuery
}

watch(filters, filterProducts)

</script>