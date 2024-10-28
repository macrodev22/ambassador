<template>
  <Nav :user="userRef" />

  <div class="container-fluid">
    <div class="row">
      <Menu />

      <main class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
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
                <tr v-for="user in users" :key="user.id">
                  <td>{{ user.id }}</td>
                  <td>{{ user.first_name + " " + user.last_name }}</td>
                  <td>{{ user.email }}</td>
                  <td><v-btn color="primary" elevation="2">View</v-btn></td>
                </tr>
              </tbody>
            </template>
          </v-table>
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import client from "@/services/axiosClient";
import router from "@/router";
import Nav from "@/components/Nav.vue";
import Menu from "@/components/Menu.vue";

const userRef = ref(null);
const users = ref([]);

// Get user
onMounted(async () => {
  try {
    const response = await client.get("/user");
    const { data: user } = response;

    userRef.value = user;

    // Get ambassadors
    const { data: ambassadors } = await client.get("/ambassadors");
    users.value = ambassadors;
  } catch (err) {
    router.push("/login");
    // console.log(err);
  }
});
</script>

<style>
.bi {
  display: inline-block;
  width: 1rem;
  height: 1rem;
}

/*
 * Sidebar
 */

@media (min-width: 768px) {
  .sidebar .offcanvas-lg {
    position: -webkit-sticky;
    position: sticky;
    top: 48px;
  }
  .navbar-search {
    display: block;
  }
}

.sidebar .nav-link {
  font-size: 0.875rem;
  font-weight: 500;
}

.sidebar .nav-link.active {
  color: #2470dc;
}

.sidebar-heading {
  font-size: 0.75rem;
}

/*
 * Navbar
 */

.navbar-brand {
  padding-top: 0.75rem;
  padding-bottom: 0.75rem;
  background-color: rgba(0, 0, 0, 0.25);
  box-shadow: inset -1px 0 0 rgba(0, 0, 0, 0.25);
}

.navbar .form-control {
  padding: 0.75rem 1rem;
}
</style>
