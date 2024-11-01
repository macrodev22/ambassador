<template>
    <table class="table table-striped">
        <thead>
            <tr>
                <th scope="col">#</th>
                <th scope="col">User</th>
                <th scope="col">Revenue</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="ranking,index in rankings" :key="ranking.name">
                <th scope="row">{{ index+1 }}</th>
                <td>{{ ranking.name }}</td>
                <td>{{ ranking.revenue }}</td>
            </tr>
        </tbody>
    </table>
</template>
<script setup>
import { ref, onMounted } from 'vue';
import client from '../services/client';

const rankings = ref([])

onMounted(async () => {
    const { data } = await client.get('/rankings')
    rankings.value = data
})
</script>