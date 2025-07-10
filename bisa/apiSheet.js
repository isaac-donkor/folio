// Define the API endpoints and their corresponding keys
const apis = [
    { url: 'https://api.example.com/first', key: 'API_KEY_1' },
    { url: 'https://api.example.com/second', key: 'API_KEY_2' },
    { url: 'https://api.example.com/third', key: 'API_KEY_3' },
    { url: 'https://api.example.com/fourth', key: 'API_KEY_4' }
  ];
  
  // Function to call all APIs (in parallel)
  export async function callAllApis() {
    try {
      const requests = apis.map(api =>
        fetch(api.url, {
          method: 'GET',
          headers: {
            'Authorization': `Bearer ${api.key}`, // Adjust if keys are in headers
            'Content-Type': 'application/json'
          }
        }).then(response => response.json())
      );
  
      const results = await Promise.all(requests);
  
      results.forEach((result, index) => {
        console.log(`API ${index + 1} result:`, result);
      });
  
      console.log("✅ All API calls completed successfully.");
    } catch (error) {
      console.error("❌ Error while calling APIs:", error);
    }
  }
  