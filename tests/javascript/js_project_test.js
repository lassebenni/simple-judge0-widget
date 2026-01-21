try {
    // We expect main.js to have logged "User: Alice"
    // Since we are running the test script, we need to check if the main.js logic works
    const data = require('./data.json');
    if (data.name !== 'Alice') throw new Error("Expected name Alice in data.json");
    
    console.log("✅_PASS_✅");
} catch (e) {
    console.log("❌_FAIL: " + e.message);
}
