import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../api";

export default function ProductDetail() {
    const { id } = useParams();
    const [product, setProduct] = useState(null);
    const [history, setHistory] = useState([]);

    // useEffect(() => {
    //     API.get(`/products/${id}`)
    //     .then(res => setProduct(res.data));

    //     API.get(`/products/${id}/history`)
    //     .then(res => setHistory(res.data));
    // }, [id]);

    useEffect(() => {
        API.get(`/products/${id}`)
            .then(res => {
                setProduct(res.data.product);
                setHistory(res.data.history);
            })
            .catch(err => console.log(err));
    }, [id]);

    if (!product) return <p>Loading...</p>;

    return (
        <div>
        <h2>{product.name}</h2>
        <p>Category: {product.category}</p>

        <h3>Price History</h3>
        <ul>
            {history.map((h, i) => (
            <li key={i}>
                {h.price} at {h.timestamp}
            </li>
            ))}
        </ul>
        </div>
    );
}