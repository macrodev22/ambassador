<template>
  <v-app>
    <main class="form-signin w-100 m-auto">
      <form @submit.prevent="onSubmit">
        <img class="mb-4" :src="Logo" alt="" width="72" height="57" />
        <h1 class="h3 mb-3 fw-normal">Please sign in</h1>

        <div class="form-floating">
          <input
            type="email"
            class="form-control"
            id="floatingInput"
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
          Sign in
        </button>
        <a href="/register">Register</a>
        <p class="mt-5 mb-3 text-body-primary">&copy; 2017–2024</p>
      </form>
      <Modal
        :title="modalTitle"
        :show="modalShow"
        :message="modalMsg"
        @close-modal="modalShow = false"
      />
    </main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import Modal from "@/components/Modal.vue";
import client from "@/services/axiosClient";
import router from "@/router";
import Logo from "@/assets/logo.svg";

const email = ref("");
const password = ref("");

const modalTitle = ref("Error! ⚠️");
const modalMsg = ref("...");
const modalShow = ref(false);

const onSubmit = () => {
  client
    .post(
      "/login",
      {
        email: email.value,
        password: password.value,
      },
      { withCredentials: true }
    )
    .then(async (res) => {
      console.log(res);
      await router.push("/");
    })
    .catch((err) => {
      modalMsg.value = err.response.data;
      modalShow.value = true;
    });
};
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

.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}

.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
</style>
