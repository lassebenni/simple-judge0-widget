try {
    if (typeof checkGrade !== 'function') {
        throw new Error("Function 'checkGrade' is missing.");
    }

    // Test cases
    const tests = [
        { in: 80, out: 'Passed' },
        { in: 60, out: 'Passed' },
        { in: 59, out: 'Failed' },
        { in: 0, out: 'Failed' }
    ];

    tests.forEach(t => {
        const res = checkGrade(t.in);
        if (res !== t.out) {
            throw new Error(`for score ${t.in}, expected '${t.out}' but got '${res}'`);
        }
    });

    console.log("✅_PASS_✅");
} catch (e) {
    console.log("❌_FAIL: " + e.message);
}
