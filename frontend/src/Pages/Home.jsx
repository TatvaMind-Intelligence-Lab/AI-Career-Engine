import About from "../Components/Home/About";
import Contact from "../Components/Home/Contact";
import Hero from "../Components/Home/Hero";
import Pricing from "../Components/Home/Pricing";

export default function Home() {

  return (
    <div className="space-y-10">
      <Hero />
      <About />
      <Pricing />
      <Contact />
    </div>
  );
}