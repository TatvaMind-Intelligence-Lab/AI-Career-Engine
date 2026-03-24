import { useState } from "react";
import LoginForm from "../Components/auth/LoginForm";
import SignupForm from "../Components/auth/SignupForm";
import { Navigate } from "react-router-dom";

export default function Auth() {
  const [isLogin, setIsLogin] = useState(true);

  const token = localStorage.getItem("token");

  if (token) {
    return <Navigate to="/dashboard" />;
  }

  return (
    <div className="flex items-center justify-center min-h-screen bg-gray-100">
      <div className="bg-white p-6 rounded-xl shadow w-full max-w-md">
        <h2 className="text-2xl font-bold text-center mb-4">
          {isLogin ? "Login" : "Sign Up"}
        </h2>

        {isLogin ? <LoginForm /> : <SignupForm />}

        {/* Toggle */}
        <p className="text-sm text-center mt-4">
          {isLogin ? "Don't have an account?" : "Already have an account?"}
          <button
            onClick={() => setIsLogin(!isLogin)}
            className="text-blue-600 ml-1"
          >
            {isLogin ? "Sign Up" : "Login"}
          </button>
        </p>
      </div>
    </div>
  );
}
