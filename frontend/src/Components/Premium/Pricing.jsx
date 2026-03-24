export default function PricingCard({
  title,
  price,
  features = [],
  isPremium = false,
  onClick,
  disabled = false,
}) {
  return (
    <div
      className={`rounded-2xl p-6 shadow-lg border transition-all duration-300 ${
        isPremium
          ? "border-blue-600 scale-105 bg-gradient-to-br from-blue-50 to-white"
          : "border-gray-200 bg-white"
      }`}
    >
      {/* Plan Title */}
      <h3 className="text-xl font-bold text-center mb-2">{title}</h3>

      {/* Price */}
      <div className="text-center mb-4">
        <span className="text-3xl font-bold">{price}</span>
        {price !== "Free" && (
          <span className="text-sm text-gray-500"> / month</span>
        )}
      </div>

      {/* Features */}
      <ul className="space-y-2 text-sm text-gray-700 mb-6">
        {features.map((feature, index) => (
          <li key={index} className="flex items-start gap-2">
            <span className="text-green-500">✔</span>
            <span>{feature}</span>
          </li>
        ))}
      </ul>

      {/* CTA Button */}
      <button
        onClick={onClick}
        disabled={disabled}
        className={`w-full py-2 rounded-lg font-semibold transition ${
          isPremium
            ? "bg-blue-600 text-white hover:bg-blue-700"
            : "bg-gray-200 text-gray-700 hover:bg-gray-300"
        } ${disabled ? "opacity-50 cursor-not-allowed" : ""}`}
      >
        {isPremium ? "Upgrade Now" : "Current Plan"}
      </button>
    </div>
  );
}
