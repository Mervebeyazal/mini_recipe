import { defineConfig } from 'cypress';
export default defineConfig({
  viewportWidth: 390,
  viewportHeight: 844,
  video: true,
  screenshotOnRunFailure: true,
  e2e: { baseUrl: 'http://localhost:5173', defaultCommandTimeout: 10000 }
});
