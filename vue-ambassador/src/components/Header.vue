<template>
    <section class="py-5 text-center container">
        <div class="row py-lg-5">
            <div class="col-lg-6 col-md-8 mx-auto">
                <h1 class="fw-light">{{title}}</h1>
                <p class="lead text-body-secondary">{{description}}</p>
            </div>
        </div>
    </section>
</template>
<script setup>
import { ref, computed, watch, onMounted } from 'vue'
import useStore from '../store';

const title = ref('')
const description = ref('')

const store = useStore()
const user = computed(() => store.auth.user )

const updateDetails = () => {

    title.value = user.value ? `$${user.value.revenue || 0 }`  : 'Welcome'

    description.value = user.value ? `You have earned this sofar` : 'Share links to earn money'
}
onMounted(updateDetails)

watch(user, updateDetails)

</script>