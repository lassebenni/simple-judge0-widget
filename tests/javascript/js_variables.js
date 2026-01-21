try {
    // 1. Check for 'firstName'
    if (typeof firstName === 'undefined') {
        throw new Error("Variable 'firstName' is missing.");
    }
    if (firstName !== 'Alice') {
        throw new Error("Expected firstName to be 'Alice', but got '" + firstName + "'.");
    }

    // 2. Check for 'minutes' and 'seconds'
    if (typeof minutes === 'undefined') throw new Error("Variable 'minutes' is missing.");
    if (typeof seconds === 'undefined') throw new Error("Variable 'seconds' is missing.");

    if (minutes !== 10) throw new Error("Expected 'minutes' to be 10.");
    if (seconds !== 600) throw new Error("Expected 'seconds' to be 600 (10 * 60).");

    console.log("✅_PASS_✅");
} catch (e) {
    console.log("❌_FAIL: " + e.message);
}
