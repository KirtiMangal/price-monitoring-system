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

//     return (
//         <div>
//             <h2>Dashboard</h2>
//             <pre>{JSON.stringify(data, null, 2)}</pre>
//         </div>
//     );


return (
    <div style={{ padding: "20px" }}>
        <h2>Dashboard</h2>

        <div style={{ display: "flex", gap: "20px" }}>
            <div style={{
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "8px"
            }}>
                <h3>Total Products</h3>
                <p>{data.total_products}</p>
            </div>

            <div style={{
                padding: "20px",
                border: "1px solid #ddd",
                borderRadius: "8px"
            }}>
                <h3>Average Price</h3>
                <p>{data.avg_price}</p>
            </div>
        </div>
    </div>
);


}