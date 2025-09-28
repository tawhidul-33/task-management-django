/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",  //templates for the root level
    "./**/templates/**/*.html", //templates inside apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}

