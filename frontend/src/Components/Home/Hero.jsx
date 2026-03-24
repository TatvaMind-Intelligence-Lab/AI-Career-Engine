import { useNavigate } from "react-router-dom";

export default function Hero() {
  const navigate = useNavigate();

  return (
    <section className="text-center py-16 space-y-6">
      <h1 className="text-5xl font-bold leading-tight">
        AI Resume Analyzer for ATS Optimization 🚀
      </h1>

      <p className="text-gray-600 max-w-xl mx-auto">
        Analyze your resume with AI, match job descriptions, and improve your
        chances of getting hired faster.
      </p>

      <button
        onClick={() => navigate("/auth")}
        className="bg-blue-600 text-white px-6 py-3 rounded-lg text-lg"
      >
        Analyze My Resume
      </button>
    </section>
  );
}
