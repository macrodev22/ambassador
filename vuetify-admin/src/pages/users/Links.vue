<template>
    <v-container>
        <v-row align="center" justify="center">
            <v-col cols="auto">
                <v-btn density="default" href="/">Back to Ambassadors</v-btn>
            </v-col>
        </v-row>
    </v-container>
    <v-table height="40rem" fixed-header>
        <thead>
            <tr>
                <th class="text-left">#</th>
                <th class="text-left">Code</th>
                <th class="text-left">Count</th>
                <th class="text-left">Revenue</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="link in links" :key="link.id">
                <td>{{ link.id }}</td>
                <td>{{ link.code }}</td>
                <td>{{ link.orders?.length || 0 }}</td>
                <td>{{ link.orders?.reduce((s, o) =>s+ o.total , 0) || 0 }}</td>
            </tr>
        </tbody>
    </v-table>
</template>

<script setup>
import client from '@/services/axiosClient';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const links = ref([])
const route = useRoute()

onMounted(async () => {
    const { data } = await client.get(`users/${route.params.id}/links`)
    links.value = data
})

</script>
