import ScoreCircle from "./ScoreCircle";

export default function ResultCard({ data, retrieval }) {
  if (!data) return null;

  return (
    <div className="mt-6 space-y-6">
      <ScoreCircle score={data.score} />

      {/* Missing Keywords */}
      <div>
        <h3 className="font-semibold">Missing Keywords</h3>
        <ul className="list-disc pl-5">
          {data.missing_keywords.map((k, i) => (
            <li key={i}>{k}</li>
          ))}
        </ul>
      </div>

      {/* Suggestions */}
      <div>
        <h3 className="font-semibold">Suggestions</h3>
        <ul className="list-disc pl-5">
          {data.suggestions.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>
      </div>

      {/* Rewritten Points */}
      <div>
        <h3 className="font-semibold">Improved Points</h3>

        <ul className="space-y-2">
          {data.rewritten_points.map((point, i) => (
            <li
              key={i}
              className="flex justify-between items-start bg-gray-100 p-3 rounded"
            >
              <span className="text-sm">{point}</span>

              <button
                onClick={() => navigator.clipboard.writeText(point)}
                className="text-xs bg-blue-500 text-white px-2 py-1 rounded ml-2 hover:bg-blue-600"
              >
                Copy
              </button>
            </li>
          ))}
        </ul>
      </div>

      {/* Retrieval (Optional Explainability) */}
      {retrieval?.length > 0 && (
        <div>
          <h3 className="font-semibold">Analyzed Sections</h3>

          {retrieval.map((item, i) => (
            <div key={i} className="bg-gray-100 p-3 rounded mb-2">
              <p className="text-xs text-gray-500">
                Score: {item.final_score.toFixed(2)}
              </p>
              <p>{item.text}</p>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
