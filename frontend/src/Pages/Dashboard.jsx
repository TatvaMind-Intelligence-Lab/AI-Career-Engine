import { useState, useEffect } from "react";
import UploadForm from "../Components/UploadForm";
import ResultCard from "../Components/ResultCard";
import Pricing from "../Components/Home/Pricing";
import PremiumPopup from "../Components/Premium/Premiumpopup";

export default function Dashboard() {
  const [result, setResult] = useState(null);
  const [retrieval, setRetrieval] = useState([]);
  const [showPremium, setShowPremium] = useState(false);

  // 🔥 Show modal once per session
  useEffect(() => {
    const shown = sessionStorage.getItem("premium_shown");

    if (!shown) {
      setShowPremium(true);
      sessionStorage.setItem("premium_shown", "true");
    }
  }, []);
  // eslint-disable-next-line react-hooks/exhaustive-deps

  return (
    <div className="p-6 space-y-10">
      {/* TOP: Upload + Results */}
      <div className="grid md:grid-cols-2 gap-6">
        {/* Upload */}
        <div className="bg-white p-4 rounded shadow">
          <UploadForm
            setResult={setResult}
            setRetrieval={setRetrieval}
            setShowPremium={setShowPremium}
          />
        </div>

        {/* Results */}
        <div className="bg-white p-4 rounded shadow">
          <ResultCard
            data={result}
            retrieval={retrieval}
            premium={showPremium}
          />
        </div>
      </div>

      {/* 🔥 PRICING (UPSELL) */}
      <Pricing />

      {/* 🔥 PREMIUM MODAL */}
      <PremiumPopup
        isOpen={showPremium}
        onClose={() => setShowPremium(false)}
        onUpgrade={() => {
          console.log("Trigger Razorpay");
        }}
      />
    </div>
  );
}
