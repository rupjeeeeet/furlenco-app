import { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard";

export default function Home() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/products")
      .then((res) => res.json())
      .then((data) => {
        console.log("Products received:", data);
        setProducts(data);
      })
      .catch((err) => console.error("Error fetching products:", err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1 style={{ color: "white", marginBottom: "20px" }}>Explore Products</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill, minmax(250px, 1fr))",
          gap: "20px",
        }}
      >
        {products.map((p) => (
          <ProductCard key={p.id} product={p} />
        ))}
      </div>
    </div>
  );
}
