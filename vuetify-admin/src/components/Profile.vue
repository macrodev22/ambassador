<template>
  <h3 class="mt-4">User Information</h3>
  <form @submit.prevent="updateUserDetails">
    <v-text-field
      label="First Name"
      v-model="user.first_name"
    ></v-text-field>

    <v-text-field
      label="Last Name"
      v-model="user.last_name"
    ></v-text-field>

    <v-text-field
      label="E-mail"
      v-model="user.email"
    ></v-text-field>

    <v-checkbox
      label="Ambassador"
      type="checkbox"
      v-model="user.is_ambassador"
      disabled="true"
    ></v-checkbox>

    <v-btn
      type="submit"
    >
      submit
    </v-btn>

  </form>

  <h3 class="mt-4">Change password</h3>
  <form @submit.prevent="updatePassword">
    <v-text-field label="Password" type="password" v-model="user.password">
    </v-text-field>
    <v-text-field label="Confirm Password" type="password" v-model="user.password_confirm"></v-text-field>

    <v-btn type="submit" >submit</v-btn>
  </form>
</template>
<script setup>
import { ref, reactive, onMounted } from 'vue'
import client from '@/services/axiosClient';
import { useRouter } from 'vue-router';

const router = useRouter()

const user = reactive({ 
  first_name: '',
  last_name: '',
  is_ambassador: false,
  email: '',
  password: '',
  password_confirm: ''
 })

onMounted(async () => {
  const { data } = await client.get('/user') 
  user.first_name = data.first_name
  user.last_name = data.last_name
  user.email = data.email

})


const updateUserDetails = async () => {
  const { data } = await client.put(`/users/info`, { email: user.email, first_name: user.first_name, last_name: user.last_name })
  await router.push('/')
}

const updatePassword = async () => {
  try {
    const { data } = await client.put('/users/password', { password: user.password, password_confirm: user.password_confirm })
    await router.push('/')
  } catch(err) {
    alert(`${err}`)
  }
}

</script>
