import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import SkeletonCard from "../components/SkeletonCard";

export default function ProductDetail() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/products/${id}`)
      .then((res) => res.json())
      .then((data) => setProduct(data));
  }, [id]);

  if (!product) return <div className="p-6"><SkeletonCard /></div>;

  return (
    <div className="p-6">
      <img
        src={product.image_url}
        className="w-full max-w-lg rounded-lg shadow-lg"
      />

      <h1 className="text-3xl font-bold mt-4">{product.title}</h1>

      <p className="text-yellow-300 text-xl font-bold mt-2">
        ₹{product.price}
      </p>

      <p className="mt-4 text-neutral-300">{product.description}</p>

      {product.features && (
        <ul className="mt-4 list-disc pl-6 text-neutral-400">
          {product.features.map((f, i) => (
            <li key={i}>{f}</li>
          ))}
        </ul>
      )}
    </div>
  );
}
