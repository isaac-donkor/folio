// Import the API calling function from another file (apiSheet.js)
import { callAllApis } from './apiSheet.js';

// Set up the button click event
document.getElementById('runApisBtn').addEventListener('click', async () => {
  try {
    await callAllApis(); // Run the API calls
  } catch (error) {
    console.error("Failed to run APIs:", error);
  }
});
