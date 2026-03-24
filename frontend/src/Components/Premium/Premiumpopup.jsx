import Modal from "../commons/Modal";

export default function PremiumPopup({ isOpen, onClose, onUpgrade }) {
  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div className="text-center space-y-4">
        {/* Title */}
        <h2 className="text-2xl font-bold">Upgrade to Premium 🚀</h2>

        {/* Description */}
        <p className="text-gray-600">
          Unlock faster AI analysis, better accuracy, and full history tracking.
        </p>

        {/* Features */}
        <div className="text-left space-y-2 text-sm text-gray-700">
          <p>✅ Faster responses (API LLM)</p>
          <p>✅ Unlimited resume analysis</p>
          <p>✅ Access past results (30 days)</p>
          <p>✅ Priority processing</p>
        </div>

        {/* Pricing */}
        <div className="text-xl font-semibold">₹199 / month</div>

        {/* CTA */}
        <button
          onClick={onUpgrade}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg w-full hover:bg-blue-700"
        >
          Upgrade Now
        </button>

        {/* Cancel */}
        <button
          onClick={onClose}
          className="text-sm text-gray-500 hover:underline"
        >
          Maybe later
        </button>
      </div>
    </Modal>
  );
}
