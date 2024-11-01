<template>
    <h3>Account Informaton</h3>
    <form @submit.prevent="submitUserInfo">
        <div class="mb-3">
            <label>First name</label>
            <input type="text" class="form-control" v-model="firstName">
        </div>
        <div class="mb-3">
            <label>Last Name</label>
            <input type="text" class="form-control" v-model="lastName">
        </div>
        <div class="mb-3">
            <label>Email</label>
            <input type="text" class="form-control" v-model="email">
        </div>

        <button class="btn btn-outline-secondary" type="submit">Save</button>
    </form>

    <h3 class="mt-4">Change Password</h3>
    <form @submit.prevent="submitPasswordInfo">
        <div class="mb-3">
            <label>Password</label>
            <input type="password" class="form-control" v-model="passwordInfo.password">
        </div>
        <div class="mb-3">
            <label>Password Confirmation</label>
            <input type="password" class="form-control" v-model="passwordInfo.password_confirm">
        </div>

        <button class="btn btn-outline-secondary" type="submit">Save</button>
    </form>
</template>
<script setup>
import { ref, reactive } from 'vue'
import client from '../services/client';
import useStore from '../store';

const store = useStore()

const firstName =  ref(store.auth.user.first_name)
const lastName =  ref(store.auth.user.last_name)
const email =  ref(store.auth.user.email)

const passwordInfo = reactive({ password:'', password_confirm:'' })

const submitUserInfo = async () => {
    await client.put('/users/info', { first_name: firstName.value, last_name: lastName.value, email: email.value })
    const { data } = await client.get('/user')
    store.auth.user = data
    localStorage.setItem('user', JSON.stringify(data))
}

const submitPasswordInfo = async () => {
    await client.put('/users/password', passwordInfo)
    passwordInfo.password = ''
    passwordInfo.password_confirm = ''
}

</script>