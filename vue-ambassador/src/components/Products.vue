<template>
    <div class="input-group mb-3">
        <span class="input-group-text" id="inputGroup-sizing-default">Search</span>
        <input type="text" class="form-control" aria-label="Sizing example input"
            aria-describedby="inputGroup-sizing-default" @keyup="updateSearchQuery" v-model="searchQuery">
    </div>
    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-3">
        <div class="col" v-for="product in products" :key="product.id">
            <div class="card shadow-sm">
                <img :src="product.image" height="200" />
                <div class="card-body">
                    <p class="card-text h5">{{ product.title }}</p>
                    <p class="card-text">{{ product.description }}</p>
                    <div class="d-flex justify-content-end align-items-center">
                        <small class="text-body-secondary">UGX {{ product.price }}</small>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script setup>
import { ref } from 'vue';

const searchQuery = ref('')

const { products } = defineProps({ products: { type: Array, default: [] } })

const emit = defineEmits(['set-search-filter'])


let timeout

const updateSearchQuery = () => {
    clearTimeout(timeout)
    setTimeout(() => emit('set-search-filter', searchQuery.value), 800)
}

</script>