module.exports = {
  purge: {
    mode: "layers",
    content: ["./public/**/*.html", "./src/**/*vue"],
  },
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        green: {
          lime: "#32cd32",
        },
      },
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
};
