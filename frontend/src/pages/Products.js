import { useEffect, useState } from "react";
import API from "../api";
import { Link } from "react-router-dom";

export default function Products() {
    const [products, setProducts] = useState([]);

    useEffect(() => {
        API.get("/products")
        .then(res => {
            console.log("DATA:", res.data);
            setProducts(res.data);
        })
        .catch(err => console.log(err));
    }, []);

    return (
        <div>
            <h2>Products</h2>

            <table border="1">
                <thead>
                <tr>
                    <th>Name</th>
                    <th>Category</th>
                    <th>Price</th>
                    <th>View</th>
                </tr>
                </thead>

                <tbody>
                {products.map(p => (
                    <tr key={p.id}>
                    <td>{p.name}</td>
                    <td>{p.category}</td>
                    <td>{p.current_price}</td>
                    <td>
                        <Link to={`/products/${p.id}`}>Details</Link>
                    </td>
                    </tr>
                ))}
                </tbody>
            </table>
        </div>
    );
}