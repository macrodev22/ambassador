<template>
  <div class="mt-4">
    <v-expansion-panels class="mb-6">
      <v-expansion-panel v-for="order in orders" :key="order.id">
        <v-expansion-panel-title expand-icon="mdi-menu-down">
          {{ order.name }}, {{ Number(order.total).toLocaleString('en-US') }}/=
        </v-expansion-panel-title>
        <v-expansion-panel-text>
          <v-table theme="dark">
            <thead>
              <tr>
                <th class="text-left">#</th>
                <th class="text-left">Product Title</th>
                <th class="text-left">Quantity</th>
                <th class="text-left">Price</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in order.order_items" :key="item.id">
                <td>{{ item.id }}</td>
                <td>{{ item.product_title }}</td>
                <td>{{ item.quantity}}</td>
                <td>{{ item.price }}</td>
              </tr>
            </tbody>
          </v-table>
        </v-expansion-panel-text>
      </v-expansion-panel>
    </v-expansion-panels>

  </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import client from '@/services/axiosClient';

const orders = ref([])

onMounted(async () => {
  const { data } = await client.get('orders')
  orders.value = data
})

</script>