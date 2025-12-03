export default function SkeletonCard() {
  return (
    <div className="product-card">
      <div className="skeleton skeleton-img"></div>
      <div className="skeleton skeleton-line"></div>
      <div className="skeleton skeleton-line" style={{ width: "50%" }}></div>
    </div>
  );
}
