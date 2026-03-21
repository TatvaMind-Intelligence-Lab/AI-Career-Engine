import { useState } from "react";
import { analyzeResume } from "../services/api";

export default function UploadForm({ setResult, setRetrieval }) {
  const [file, setFile] = useState(null);
  const [jd, setJd] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file || !jd) {
      return alert("Please upload resume and enter JD");
    }

    setLoading(true);

    try {
      const res = await analyzeResume(file, jd);

      setResult(res.data);
      setRetrieval(res.retrieval || []);
    } catch (err) {
      console.error(err);
      alert("Something went wrong");
    }

    setLoading(false);
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow space-y-4">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full"
      />

      <textarea
        placeholder="Paste Job Description..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        className="w-full h-32 border p-2 rounded"
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        className={`px-4 py-2 rounded w-full text-white ${
          loading ? "bg-gray-400" : "bg-blue-600 hover:bg-blue-700"
        }`}
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {/* Loader Indicator */}
      {loading && (
        <div className="text-center mt-2 text-sm text-gray-500 animate-pulse">
          Processing your resume...
        </div>
      )}
    </div>
  );
}
