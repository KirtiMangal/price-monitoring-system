import React from "react";
import { useEffect, useState } from "react";
import API from "../api";

export default function Dashboard() {
    const [data, setData] = useState(null);

    useEffect(() => {
        API.get("/analytics")
            .then(res => setData(res.data))
            .catch(err => console.log(err));
    }, []);

    if (!data){
        return <p>Loading...</p>;
    }

    return (
        <div>
            <h2>Dashboard</h2>
            <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
    );
}