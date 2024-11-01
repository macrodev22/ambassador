<template>
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">Link</th>
                <th scope="col">Users</th>
                <th scope="col">Revenue</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="link in links" :key="link.code">
                <td>{{linkUrl(link)}}</td>
                <td>{{link.users}}</td>
                <td>{{link.revenue}}</td>
            </tr>
            
        </tbody>
    </table>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import client from '../services/client';

// link <id, code, users, revenue>
const links = ref([])

onMounted(async () => {
    const { data } = await client.get('/stats')

    links.value = data
})

const linkUrl = (link) => `http://localhost:8000/links/${link.code}`

</script>