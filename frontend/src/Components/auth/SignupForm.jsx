import { useState } from "react";
import { signup } from "../../Services/auth"; // ✅ FIXED
import { useNavigate } from "react-router-dom";
import toast from "react-hot-toast";

export default function SignupForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  const handleSignup = async () => {
    if (!email || !password) {
      toast.error("Please enter email and password");
      return;
    }

    setLoading(true);

    try {
      const res = await signup(email, password);

      if (res?.status === "success") {
        toast.success("Signup successful! Please login.");

        navigate("/auth"); // ✅ no timeout needed
      } else {
        toast.error(res?.message || "Signup failed");
      }
    } catch (err) {
      console.error(err);
      toast.error("Signup failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="space-y-4">
      <input
        type="email"
        placeholder="Email"
        className="w-full border p-2 rounded"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      <input
        type="password"
        placeholder="Password"
        className="w-full border p-2 rounded"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />

      <button
        onClick={handleSignup}
        disabled={loading}
        className="w-full bg-green-600 text-white py-2 rounded disabled:opacity-50"
      >
        {loading ? "Signing up..." : "Sign Up"}
      </button>
    </div>
  );
}