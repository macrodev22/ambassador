import axios from "axios";

const client = axios.create({
    baseURL: 'http://localhost:8000/api/admin',
    withCredentials: true,
})

export default client;