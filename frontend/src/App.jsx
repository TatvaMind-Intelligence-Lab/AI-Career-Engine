import { BrowserRouter, Routes, Route } from "react-router-dom";
import Navbar from "./Components/commons/Navbar";
import Home from "./Pages/Home";
import Auth from "./Pages/Auth";
import Dashboard from "./Pages/Dashboard";
import ProtectedRoute from "./Components/auth/protectedRoutes";

function App() {
  return (
    <BrowserRouter>
      <Navbar />

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/auth" element={<Auth />} />
        <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
