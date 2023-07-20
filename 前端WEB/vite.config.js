import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import WindiCSS from "vite-plugin-windicss";
// https://vitejs.dev/config/
export default defineConfig({
  server: {
    watch: {
      usePolling: true, // 修复HMR热更新失效
    },
  },
  plugins: [vue(), WindiCSS()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
