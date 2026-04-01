import axios from "axios";

const API = axios.create({
    baseURL: "http://localhost:8000",
    headers: {
        "x-api-key": "secret123"
    }
});

export default API;