try:
    assert is_empty(None) is True, "is_empty(None) should be True"
    assert is_empty("") is True, "is_empty('') should be True"
    assert is_empty("text") is False, "is_empty('text') should be False"
    assert is_empty(0) is False, "is_empty(0) should be False"
    print("✅_PASS_✅")
except Exception as e:
    print(f"❌_FAIL: {e}")
