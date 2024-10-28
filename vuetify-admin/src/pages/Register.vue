<template>
  <v-app>
    <main class="form-signin w-100 m-auto">
      <form @submit.prevent="onSubmitForm">
        <h1 class="h3 mb-3 fw-normal">Register</h1>

        <div class="form-floating">
          <input
            type="text"
            class="form-control"
            placeholder="First name"
            v-model="first_name"
          />
          <label for="floatingInput">First name</label>
        </div>
        <div class="form-floating">
          <input
            type="text"
            class="form-control"
            placeholder="Last name"
            v-model="last_name"
          />
          <label for="floatingInput">Last name</label>
        </div>
        <div class="form-floating">
          <input
            type="email"
            class="form-control"
            placeholder="name@example.com"
            v-model="email"
          />
          <label for="floatingInput">Email address</label>
        </div>
        <div class="form-floating">
          <input
            type="password"
            class="form-control"
            id="floatingPassword"
            placeholder="Password"
            v-model="password"
          />
          <label for="floatingPassword">Password</label>
        </div>
        <div class="form-floating">
          <input
            type="password"
            class="form-control"
            placeholder="Password Confirm"
            v-model="password_confirm"
          />
          <label for="floatingPassword">Password Confirm</label>
        </div>

        <div class="form-check text-start my-3">
          <input
            class="form-check-input"
            type="checkbox"
            value="remember-me"
            id="flexCheckDefault"
          />
          <label class="form-check-label" for="flexCheckDefault">
            Remember me
          </label>
        </div>
        <button class="btn btn-primary w-100 py-2" type="submit">
          Register
        </button>
        <RouterLink to="/login">Login</RouterLink>
        <p class="mt-5 mb-3 text-body-primary">&copy; 2017–2024</p>
      </form>
      <Modal
        :show="showModal"
        :message="modalMsg"
        :title="modalTitle"
        @close-modal="showModal = false"
      />
    </main>
  </v-app>
</template>
<script setup>
import { ref } from "vue";

import Modal from "@/components/Modal.vue";

import client from "@/services/axiosClient";
import router from "@/router";

const first_name = ref("");
const last_name = ref("");
const email = ref("");
const password = ref("");
const password_confirm = ref("");

const showModal = ref(false);
const modalTitle = ref("An error has occured!⚠️");
const modalMsg = ref("......");

const onSubmitForm = () => {
  client
    .post(
      "/register",
      {
        first_name: first_name.value,
        last_name: last_name.value,
        email: email.value,
        password: password.value,
        password_confirm: password_confirm.value,
      },
      { headers: { "Content-Type": "application/json" } }
    )
    .then((res) => {
      // console.log(res);
      router.push("/login");
    })
    .catch((err) => {
      console.error(err);
      console.log(err.response.data);
      modalMsg.value = err.response.data;
      showModal.value = true;
    });
};
//
</script>

<style>
html,
body {
  height: 100%;
}

.form-signin {
  max-width: 330px;
  padding: 1rem;
}

.form-signin .form-floating:focus-within {
  z-index: 2;
}

.form-floating input {
  border-radius: 0;
}

.form-floating:first-of-type input {
  border-top-left-radius: var(--bs-border-radius);
  border-top-right-radius: var(--bs-border-radius);
}

/* Last input box */
.form-floating:has(#floatingPassword) ~ .form-floating input {
  border-bottom-left-radius: var(--bs-border-radius);
  border-bottom-right-radius: var(--bs-border-radius);
}

/* --bs-border-radius: 0.375rem; */
/* .form-floating > .form-control::placeholder,
.form-floating > .form-control-plaintext::placeholder {
  color: var(--bs-tertiary-color);
} */
</style>
