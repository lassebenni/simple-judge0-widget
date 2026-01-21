import sys

def test():
    try:
        # Check if function exists in globals (Simple Mode) or via import (Project Mode)
        func = None
        if 'calculate_stats' in globals():
            func = globals()['calculate_stats']
        else:
            try:
                import main
                func = getattr(main, 'calculate_stats', None)
            except ImportError:
                pass
        
        if not func:
            print("❌_FAIL: Function 'calculate_stats' not found. Ensure it is defined in main.py")
            return
        
        # Test 1: Basic
        res1 = func([10, 20, 30])
        # Default state returns (0, 0), so this will fail as expected.
        if res1 != (60, 20.0):
            print(f"❌_FAIL: Expected (60, 20.0) for [10, 20, 30], got {res1}")
            return

        # Test 2: Rounded
        res2 = func([1, 2, 4], rounded=True)
        if res2 != (7, 2):
            print(f"❌_FAIL: Expected (7, 2) for [1, 2, 4] with rounded=True, got {res2}")
            return
            
        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: Error during execution: {str(e)}")

if __name__ == "__main__":
    test()
