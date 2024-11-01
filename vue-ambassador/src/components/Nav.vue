<template>
    <div class="container">
        <header
            class="d-flex flex-wrap align-items-center justify-content-center justify-content-md-between py-3 mb-4 border-bottom">

            <ul class="nav col-12 col-md-auto mb-2 justify-content-center mb-md-0">
                <li><RouterLink to="/" class="nav-link px-2">Frontend</RouterLink></li>
                <li><RouterLink to="/backend" class="nav-link px-2">Backend</RouterLink></li>
            </ul>

            <div class="col-md-6 text-end" v-if="user">
                <RouterLink to="/stats" class="btn btn-light me-2">Stats</RouterLink>
                <RouterLink to="/rankings" class="btn btn-light me-2">Rankings</RouterLink>
                <RouterLink to="/profile" class="btn btn-primary me-2">{{ user.first_name }} {{ user.last_name }}</RouterLink>
                <button type="button" class="btn btn-outline-primary" @click="logout">Logout</button>
            </div>
            <div class="col-md-3 text-end" v-else>
                <RouterLink to="/login" type="button" class="btn btn-outline-primary me-2">Login</RouterLink>
                <RouterLink to="/register" type="button" class="btn btn-primary">Sign-up</RouterLink>
            </div>
        </header>
    </div>
</template>

<script setup>
import {  computed } from 'vue';
import { RouterLink, useRouter, } from 'vue-router';
import useStore from '../store';
import client from '../services/client';

const store = useStore()

const user = computed(() => store.auth.user)

const router = useRouter()

const logout = () => {
    client.post('/logout')
    .then(() => {
        localStorage.removeItem('user')
        router.push('/login')
    })
}
</script>