import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import ProductDetail from "./pages/ProductDetail";
import Chat from "./pages/Chat";

export default function App() {
  return (
    <div className="app-container">
      <BrowserRouter>
        <Navbar />

        <main className="page-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/product/:id" element={<ProductDetail />} />
            <Route path="/chat" element={<Chat />} />
          </Routes>
        </main>
      </BrowserRouter>
    </div>
  );
}
