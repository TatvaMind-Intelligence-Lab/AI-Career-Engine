import PricingCard from "../Premium/Pricing";

export default function Pricing() {
  return (
    <section className="py-16 bg-gray-50">
      
      <h2 className="text-3xl font-bold text-center mb-10">
        Pricing Plans
      </h2>

      <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">

        {/* FREE PLAN */}
        <PricingCard
          title="Free"
          price="Free"
          features={[
            "2 analyses per month",
            "Basic AI insights",
            "No history tracking",
          ]}
          disabled={true}
        />

        {/* PREMIUM PLAN */}
        <PricingCard
          title="Premium"
          price="₹199"
          isPremium={true}
          features={[
            "Unlimited analyses",
            "Advanced AI insights",
            "History tracking",
            "Faster processing",
          ]}
          onClick={() => {
            console.log("Upgrade clicked");
            // later → Razorpay integration
          }}
        />

      </div>

    </section>
  );
}