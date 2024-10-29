<template>
  <header
    class="navbar sticky-top bg-dark flex-md-nowrap p-0 shadow"
    data-bs-theme="dark"
  >
    <a class="navbar-brand col-md-3 col-lg-2 me-0 px-3 fs-6 text-white" href="#"
      >Hello, {{ user ? user.first_name : "User" }}</a
    >
    <nav class="my-2 my-md-0 mr-md-3">
      <RouterLink to="/profile" class="p-2 text-white text-decoration-none"
        >{{ user && user.first_name + " " + user.last_name }}
      </RouterLink>
      <a href="#" class="p-2 text-white text-decoration-none" @click="logout">Log out </a>
    </nav>
    <ul class="navbar-nav flex-row d-md-none">
      <li class="nav-item text-nowrap">
        <button
          class="nav-link px-3 text-white"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSearch"
          aria-controls="navbarSearch"
          aria-expanded="false"
          aria-label="Toggle search"
        >
          {{ user && user.first_name
          }}<svg class="bi"><use xlink:href="#search" /></svg>
        </button>
      </li>
      <li class="nav-item text-nowrap">
        <button
          class="nav-link px-3 text-white"
          type="button"
          data-bs-toggle="offcanvas"
          data-bs-target="#sidebarMenu"
          aria-controls="sidebarMenu"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <svg class="bi"><use xlink:href="#list" /></svg>
        </button>
      </li>
    </ul>

    <div id="navbarSearch" class="navbar-search w-100 collapse">
      <input
        class="form-control w-100 rounded-0 border-0"
        type="text"
        placeholder="Search"
        aria-label="Search"
      />
    </div>
  </header>
</template>

<script setup>
import { defineProps } from "vue";
import { useRouter } from "vue-router";
import client from "@/services/axiosClient";

const props = defineProps({
  user: Object,
});

const router = useRouter()

const logout = async () => {
  await client.post('/logout')
  await router.push('/login')
}
</script>
