<template>
    <v-table theme="dark">
        <thead>
            <tr>
                <th class="text-left">#</th>
                <th class="text-left">Image</th>
                <th class="text-left">Title</th>
                <th class="text-left">Description</th>
                <th class="text-left">Price</th>
                <th class="text-left">Actions</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="product in products.slice((page-1)*perPage, page*perPage)" :key="product.id">
                <td>{{ product.id }}</td>
                <td><v-img :src="product.image" max-height="80" max-width="120" /></td>
                <td>{{ product.title }}</td>
                <td>{{ product.description }}</td>
                <td>{{ product.price }}/=</td>
                <td><v-btn icon="mdi-trash-can" color="error" size="small" @click="deleteProduct(product.id)"></v-btn></td>
            </tr>
        </tbody>
    </v-table>
    <v-pagination :length="pages" v-model="page"></v-pagination>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import client from '@/services/axiosClient';
import { useRouter } from 'vue-router';

const products = ref([])
const router = useRouter()

//Pagination
const page = ref(1)
const perPage = ref(10)
const pages = ref(0)

onMounted(async () => {
    const { data } = await client.get('products')
    products.value = data

    pages.value = Math.ceil(data.length / perPage.value)
})

const deleteProduct = async (id) => {
    if (confirm(`Are you sure you want to delete product ${id}?`)) {
        await client.delete(`products/${id}`)
        products.value = products.value.filter((p) => p.id != id)
    }
}

</script>