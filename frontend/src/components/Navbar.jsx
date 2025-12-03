import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <div
      style={{
        background: "#111",
        padding: "15px 25px",
        display: "flex",
        gap: "30px",
        alignItems: "center",
        color: "white",
        fontSize: "18px",
        borderBottom: "1px solid #333",
      }}
    >
      <Link to="/" style={{ color: "white", textDecoration: "none" }}>
        MyStore
      </Link>

      <Link to="/chat" style={{ color: "white", textDecoration: "none" }}>
        AI Assistant 🤖
      </Link>
    </div>
  );
}
