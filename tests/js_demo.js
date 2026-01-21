try {
    if (typeof sum !== 'function') {
        throw new Error("Function 'sum' is not defined.");
    }
    
    if (sum(1, 2) !== 3) {
        throw new Error("sum(1, 2) should return 3.");
    }

    if (sum(-1, 5) !== 4) {
        throw new Error("sum(-1, 5) should return 4.");
    }

    console.log("✅_PASS_✅");
} catch (e) {
    console.log("❌_FAIL: " + e.message);
}
