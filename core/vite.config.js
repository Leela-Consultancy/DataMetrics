import { defineConfig } from 'vite';
import laravel from 'laravel-vite-plugin';

export default defineConfig({
    //root: '.', // Ensure this points to the directory containing index.html
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.js'],
            refresh: true,
        }),
    ],
    server: {
        open: true, // Automatically open the browser
        port: 4000, // Change the port to 4000
    },
});
