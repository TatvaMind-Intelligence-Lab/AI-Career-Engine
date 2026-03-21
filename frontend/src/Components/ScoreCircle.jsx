export default function ScoreCircle({ score }) {
  let color = "border-red-500 text-red-500";

  if (score >= 75) {
    color = "border-green-500 text-green-600";
  } else if (score >= 50) {
    color = "border-yellow-500 text-yellow-600";
  }

  return (
    <div className="flex items-center justify-center">
      <div
        className={`w-32 h-32 rounded-full border-8 flex items-center justify-center text-2xl font-bold ${color}`}
      >
        {score}
      </div>
    </div>
  );
}
