export default function ResultCard({ data }) {
  if (!data) return null;

  return (
    <div className="mt-6 space-y-6">
      
      {/* Score */}
      <div className="text-center">
        <h2 className="text-4xl font-bold">{data.score}</h2>
        <p className="text-gray-500">Match Score</p>
      </div>

      {/* Missing Keywords */}
      <div>
        <h3 className="font-semibold mb-2">Missing Keywords</h3>
        <div className="flex flex-wrap gap-2">
          {data.missing_keywords.map((k, i) => (
            <span key={i} className="bg-red-100 text-red-600 px-2 py-1 rounded">
              {k}
            </span>
          ))}
        </div>
      </div>

      {/* Suggestions */}
      <div>
        <h3 className="font-semibold mb-2">Suggestions</h3>
        <ul className="list-disc pl-5 space-y-1">
          {data.suggestions.map((s, i) => (
            <li key={i}>{s}</li>
          ))}
        </ul>
      </div>

      {/* Rewritten Points */}
      <div>
        <h3 className="font-semibold mb-2">Rewritten Points</h3>
        <ul className="list-disc pl-5 space-y-1">
          {data.rewritten_points.map((r, i) => (
            <li key={i}>{r}</li>
          ))}
        </ul>
      </div>

    </div>
  );
}