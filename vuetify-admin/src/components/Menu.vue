<template>
  <div
    class="sidebar border border-right col-md-3 col-lg-2 p-0 bg-body-tertiary"
  >
    <div
      class="offcanvas-md offcanvas-end bg-body-tertiary"
      tabindex="-1"
      id="sidebarMenu"
      aria-labelledby="sidebarMenuLabel"
    >
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="sidebarMenuLabel">Company name</h5>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="offcanvas"
          data-bs-target="#sidebarMenu"
          aria-label="Close"
        ></button>
      </div>
      <div
        class="offcanvas-body d-md-flex flex-column p-0 pt-lg-3 overflow-y-auto"
      >
        <ul class="nav flex-column">
          <li class="nav-item">
            <RouterLink
              class="nav-link d-flex align-items-center gap-2 active"
              aria-current="page"
              to="/users"
            >
              <svg class="bi"><use xlink:href="#house-fill" /></svg>
              Users
            </RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink
              class="nav-link d-flex align-items-center gap-2 active"
              aria-current="page"
              to="/products"
            >
              <svg class="bi"><use xlink:href="#house-fill" /></svg>
              Products
            </RouterLink>
            <RouterLink
              class="nav-link d-flex align-items-center gap-2 active"
              aria-current="page"
              to="/orders"
            >
              <svg class="bi"><use xlink:href="#house-fill" /></svg>
              Orders
            </RouterLink>
          </li>
          <li class="nav-item">
            <a
              class="nav-link d-flex align-items-center gap-2"
              href="#"
              @click="logout"
            >
              <svg class="bi"><use xlink:href="#door-closed"></use></svg>
              Sign out
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>
<script setup>
import client from "@/services/axiosClient";
import router from "@/router";
//
const props = defineProps({
  user: Object,
});

const logout = async () => {
  await client.post("/logout");
  await router.push("/login");
};
</script>
