import sys

def test():
    try:
        # Check if function exists
        if 'calculate_stats' not in globals():
            print("❌_FAIL: Function 'calculate_stats' is not defined.")
            return

        func = globals()['calculate_stats']
        
        # Test 1: Basic
        res1 = func([10, 20, 30])
        if res1 != (60, 20.0):
            print(f"❌_FAIL: Expected (60, 20.0) for [10, 20, 30], got {res1}")
            return

        # Test 2: Rounded
        res2 = func([1, 2, 4], rounded=True)
        # sum=7, avg=2.333 -> rounded avg=2
        if res2 != (7, 2):
            print(f"❌_FAIL: Expected (7, 2) for [1, 2, 4] with rounded=True, got {res2}")
            return
            
        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: {str(e)}")

if __name__ == "__main__":
    test()
