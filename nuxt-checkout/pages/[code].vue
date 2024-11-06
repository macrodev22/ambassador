<template>
    <div class="container">
        <main>
            <div class="py-5 text-center">
                <h2>Welcome</h2>
                <p class="lead">{{ ambassador?.first_name }} has invited you to buy these products</p>
            </div>

            <div class="row g-5">
                <div class="col-md-5 col-lg-4 order-md-last">
                    <h4 class="d-flex justify-content-between align-items-center mb-3">
                        <span class="text-primary">Products</span>
                        <span class="badge bg-primary rounded-pill">{{ products.length }}</span>
                    </h4>
                    <ul class="list-group mb-3">
                        <template v-for="product in products" :key="product.id">
                            <li class="list-group-item d-flex justify-content-between lh-sm" >
                                <div>
                                    <h6 class="my-0">{{product.title}}</h6>
                                    <small class="text-body-secondary">{{ product.description }}</small>
                                </div>
                                <span class="text-body-secondary">UGX {{ Number(product.price).toLocaleString('en-US') }}</span>
                            </li>
                            <li class="list-group-item d-flex justify-content-between lh-sm">
                                <div>
                                    <h6 class="my-0">Quantity</h6>
                                </div>
                                <input type="number" v-model="quantities[product.id]" min="0" class="form-control text-muted quantity">
                            </li>
                        </template>
                        <li class="list-group-item d-flex justify-content-between">
                            <span>Total (UGX)</span>
                            <strong>{{ products.reduce((s,p) => s + (p.price*quantities[p.id]), 0).toLocaleString('en-US') }}/=</strong>
                        </li>
                    </ul>

                </div>
                <div class="col-md-7 col-lg-8">
                    <h4 class="mb-3">Personal details</h4>
                    <form class="needs-validation" @submit.prevent="chechout" novalidate>
                        <div class="row g-3">
                            <div class="col-sm-6">
                                <label for="firstName" class="form-label">First name</label>
                                <input type="text" v-model="personalInfo.first_name" class="form-control" id="firstName" placeholder="" required>
                                <div class="invalid-feedback">
                                    Valid first name is required.
                                </div>
                            </div>

                            <div class="col-sm-6">
                                <label for="lastName" class="form-label">Last name</label>
                                <input type="text" v-model="personalInfo.last_name" class="form-control" id="lastName" placeholder="" required>
                                <div class="invalid-feedback">
                                    Valid last name is required.
                                </div>
                            </div>

                            <div class="col-12">
                                <label for="email" class="form-label">Email <span
                                        class="text-body-secondary">(Optional)</span></label>
                                <input type="email" v-model="personalInfo.email" class="form-control" id="email" placeholder="you@example.com">
                                <div class="invalid-feedback">
                                    Please enter a valid email address for shipping updates.
                                </div>
                            </div>

                            <div class="col-12">
                                <label for="address" class="form-label">Address</label>
                                <input type="text" v-model="personalInfo.address" class="form-control" id="address" placeholder="1234 Main St"
                                    required>
                                <div class="invalid-feedback">
                                    Please enter your shipping address.
                                </div>
                            </div>

                            <div class="col-md-5">
                                <label for="country" class="form-label">Country</label>
                                <input class="form-control" v-model="personalInfo.country" id="country" required />
                                <div class="invalid-feedback">
                                    Please select a valid country.
                                </div>
                            </div>

                            <div class="col-md-4">
                                <label for="city" class="form-label">City</label>
                                <input class="form-control" v-model="personalInfo.city" id="city" required />
                                <div class="invalid-feedback">
                                    Please provide a valid city.
                                </div>
                            </div>

                            <div class="col-md-3">
                                <label for="zip" class="form-label">Zip</label>
                                <input type="text" v-model="personalInfo.zip" class="form-control" id="zip" placeholder="" required>
                                <div class="invalid-feedback">
                                    Zip code required.
                                </div>
                            </div>
                        </div>

                        <hr class="my-4">

                        <button class="w-100 btn btn-primary btn-lg" type="submit">Checkout</button>
                    </form>
                </div>
            </div>
        </main>

        <footer class="my-5 pt-5 text-body-secondary text-center text-small">
            <p class="mb-1">&copy; 2017–2024 Company Name</p>
            <ul class="list-inline">
                <li class="list-inline-item"><a href="#">Privacy</a></li>
                <li class="list-inline-item"><a href="#">Terms</a></li>
                <li class="list-inline-item"><a href="#">Support</a></li>
            </ul>
        </footer>
    </div>
</template>

<script setup>
import { useAsyncData } from 'nuxt/app'
import { useNuxtApp } from '#app'

const route = useRoute()
const { $axios } = useNuxtApp()

const personalInfo = reactive({
    first_name: '',
    last_name: '',
    address: '',
    country: '',
    city: '',
    zip: '',
    email: ''
})

const products = ref([])
const ambassador = ref({})

const quantities = reactive({})

const code = route.params.code

const { data: linkData, error } = await useAsyncData('link', async () => {

    const { data} =  await $axios.get(`/checkout/links/${code}`)
    return data
})

// console.log(linkData, linkData.value.products)
if(error.value) {
    console.log('Error fetching link data')
} else {
    products.value = linkData.value.products
    ambassador.value = linkData.value.user
}

const chechout = async () => {

    const payload = { 
        ...personalInfo,
         code, 
        products: products.value.map(p => ({ product_id: p.id, quantity: quantities[p.id] }))
     }

    const { data } = await $axios.post('/checkout/orders', payload)

}

</script>

<style>
.quantity {
    width: 5rem;
}
</style>