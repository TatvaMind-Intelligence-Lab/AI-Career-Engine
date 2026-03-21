import { useState } from "react";
import { analyzeResume } from "../Services/api";

export default function UploadForm({ setResult, setRetrieval }) {
  const [file, setFile] = useState(null);
  const [jd, setJd] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!file || !jd) return alert("Provide both inputs");

    setLoading(true);

    const res = await analyzeResume(file, jd);

    console.log("API RESPONSE:", res);

    if (res.data) {
      setResult(res.data.analsis);
      setRetrieval(res.retrieval || []);
    }

    setLoading(false);
  };

  return (
    <div className="bg-white p-6 rounded-xl shadow-md space-y-4">
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        className="w-full"
      />

      <textarea
        placeholder="Paste Job Description..."
        value={jd}
        onChange={(e) => setJd(e.target.value)}
        className="w-full border p-3 rounded-lg h-32"
      />

      <button
        onClick={handleSubmit}
        className="bg-black text-white px-6 py-2 rounded-lg"
      >
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </div>
  );
}
