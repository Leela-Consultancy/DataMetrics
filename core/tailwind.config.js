import defaultTheme from 'tailwindcss/defaultTheme';

/** @type {import('tailwindcss').Config} */
export default {
    content: [
        "./resources/views/**/*.blade.php",
        "./resources/js/**/*.vue",
        "./public/**/*.html",
    ],
    theme: {
        extend: {},
    },
    plugins: [],
};
