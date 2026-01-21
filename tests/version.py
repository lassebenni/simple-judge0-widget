import sys
try:
    v = sys.version.split()[0]
    assert "3.11" in v, f"Expected 3.11, got {v}"
    print("✅_PASS_✅")
except Exception as e:
    print(f"❌_FAIL: {e}")
