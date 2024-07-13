/** @type {import("tailwindcss").Config} */
export default {
  content: [
    "./src/app.html",
    "./src/**/*.{svelte,js,ts,jsx,tsx}",
  ],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: "1rem",
        sm: "1rem",
        lg: "2rem",
      },
    },
    fontFamily: {
      "title": ["Neuton"],
    },
    extend: {},
  },
  plugins: [],
}
