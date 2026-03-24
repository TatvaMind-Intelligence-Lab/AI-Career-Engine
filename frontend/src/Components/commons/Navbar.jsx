import { Link } from "react-router-dom";
import useAuth from "../../hooks/useAuth";

export default function Navbar() {
  const { user, logout } = useAuth();

  return (
    <nav className="w-full px-6 py-4 flex justify-between items-center bg-white shadow-sm">
      <Link to="/" className="text-xl font-bold text-blue-600">
        TatvaMind
      </Link>

      <div className="flex items-center gap-4">
        {!user ? (
          <Link
            to="/auth"
            className="px-4 py-2 bg-blue-600 text-white rounded-lg"
          >
            Login
          </Link>
        ) : (
          <div className="flex items-center gap-3">
            {/* Avatar */}
            <div className="w-8 h-8 bg-blue-600 text-white rounded-full flex items-center justify-center">
              {user.email[0].toUpperCase()}
            </div>

            {/* Logout */}
            <button onClick={logout} className="text-sm text-gray-600">
              Logout
            </button>
          </div>
        )}
      </div>
    </nav>
  );
}
