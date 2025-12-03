export default function ProductCard({ product }) {
  return (
    <div
      style={{
        background: "#222",
        padding: "15px",
        borderRadius: "8px",
        color: "white",
      }}
    >
      <img
        src={product.images?.[0] || "https://via.placeholder.com/300x200?text=No+Image"}
        alt={product.title}
        style={{ width: "100%", height: "180px", objectFit: "cover", borderRadius: "6px" }}
      />

      <h3 style={{ marginTop: "10px" }}>{product.title}</h3>
      <p>₹{product.price}</p>
    </div>
  );
}
