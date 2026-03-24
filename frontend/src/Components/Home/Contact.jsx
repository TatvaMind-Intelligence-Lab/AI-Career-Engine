import { useState } from "react";
import toast from "react-hot-toast";

export default function Contact() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const handleSubmit = (e) => {
    e.preventDefault();

    // 🔥 for now just simulate
    toast.success("Message sent!");
    setForm({ name: "", email: "", message: "" });
  };

  return (
    <section className="py-16 max-w-xl mx-auto">
      <h2 className="text-3xl font-bold text-center mb-6">Contact Us</h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          placeholder="Your Name"
          className="w-full border p-2 rounded"
          value={form.name}
          onChange={(e) => setForm({ ...form, name: e.target.value })}
        />

        <input
          type="email"
          placeholder="Your Email"
          className="w-full border p-2 rounded"
          value={form.email}
          onChange={(e) => setForm({ ...form, email: e.target.value })}
        />

        <textarea
          placeholder="Your Message"
          className="w-full border p-2 rounded h-32"
          value={form.message}
          onChange={(e) => setForm({ ...form, message: e.target.value })}
        />

        <button className="w-full bg-blue-600 text-white py-2 rounded">
          Send Message
        </button>
      </form>
    </section>
  );
}
