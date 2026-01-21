import sys
import os

sys.path.append(os.getcwd())

def test():
    try:
        func = None
        # Try finding in globals (Simple Mode)
        if 'calculate_stats' in globals():
            func = globals()['calculate_stats']
        else:
            # Try importing (Project Mode)
            try:
                if 'main' in sys.modules: del sys.modules['main']
                import main
                func = getattr(main, 'calculate_stats', None)
            except (ImportError, Exception):
                pass
        
        if not func:
            print("❌_FAIL: Function 'calculate_stats' was not found.")
            return
        
        # Test 1: Basic
        res1 = func([10, 20, 30])
        if res1 == (0, 0):
             print("❌_FAIL: Function still returns default (0, 0). Implement the math!")
             return
        if res1 != (60, 20.0):
            print(f"❌_FAIL: Incorrect result for [10, 20, 30]. Expected (60, 20.0), got {res1}")
            return

        # Test 2: Rounded
        res2 = func([1, 2, 4], rounded=True)
        if res2 != (7, 2):
            print(f"❌_FAIL: Expected (7, 2) for [1, 2, 4] with rounded=True, got {res2}")
            return
            
        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: Execution error: {str(e)}")

if __name__ == "__main__":
    test()
