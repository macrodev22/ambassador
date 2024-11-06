import { defineNuxtPlugin } from "#app";
import axios from "axios";

const BASE_URL = 'http://localhost:8000/api'

export default defineNuxtPlugin( app => {
    const api = axios.create({
        baseURL: BASE_URL,
    })

    app.provide('axios', api)
} )