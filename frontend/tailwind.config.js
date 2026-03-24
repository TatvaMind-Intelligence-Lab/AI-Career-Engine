/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: "#0F172A", // Slate Black
        secondary: "#4F46E5", // Electric Indigo
        success: "#14B8A6", // Teal
        warning: "#F59E0B", // Amber

        background: "#F8FAFC", // Cool Grey
        card: "#1F2937", // Subtle dark grey for cards
      },

      fontFamily: {
        heading: ["Inter", "sans-serif"],
        body: ["Roboto", "sans-serif"],
      },
    },
  },
  plugins: [],
};
