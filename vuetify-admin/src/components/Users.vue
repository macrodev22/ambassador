<template>
    <div class="table-responsive small">
        <v-table>
            <template v-slot:default>
                <thead>
                    <tr>
                        <th class="text-left">#</th>
                        <th class="text-left">Name</th>
                        <th class="text-left">Email</th>
                        <th class="text-left">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="user in users.slice((currentPage - 1) * perPage, currentPage * perPage)" :key="user.id">
                        <td>{{ user.id }}</td>
                        <td>{{ user.first_name + " " + user.last_name }}</td>
                        <td>{{ user.email }}</td>
                        <td><v-btn color="primary" elevation="2" :href="`/users/${user.id}/links`">View</v-btn></td>
                    </tr>
                </tbody>
            </template>
        </v-table>
        <v-pagination :length="numPages" total-visible="10" v-model="currentPage"></v-pagination>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import client from '@/services/axiosClient';

const users = ref([]);

//Pagination
const numPages = ref(0)
const perPage = ref(10)
const currentPage = ref(1)

onMounted(async () => {
    try {
        // Get ambassadors
    const { data: ambassadors } = await client.get("/ambassadors");
    users.value = ambassadors;
    numPages.value = Math.ceil(ambassadors.length / perPage.value)
    } catch(err) {
        console.error(err)
    }
})

</script>