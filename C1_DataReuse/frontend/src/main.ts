import "bootstrap-italia/dist/css/bootstrap-italia.min.css";
import "bootstrap-italia/dist/js/bootstrap-italia.bundle.min.js";

import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

const app = createApp(App);

app.use(router);

app.mount("#app");
