import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./Components/commons/Navbar";
import Home from "./Pages/Home";
import Auth from "./Pages/Auth";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;