try:
    if 'result' not in locals():
        raise Exception("Variable 'result' is missing. Did you delete it?")
    
    expected = [10, 20]
    assert result == expected, f"Expected {expected}, got {result}. Did you skip negatives and break at > 50?"
    print("✅_PASS_✅")
except Exception as e:
    print(f"❌_FAIL: {e}")
