import io
import sys
import os
from contextlib import redirect_stdout

# Ensure we can import from the current directory
sys.path.append(os.getcwd())

def test():
    try:
        # 1. Check for prints during import
        f = io.StringIO()
        with redirect_stdout(f):
            try:
                # If 'main' was already imported (somehow), reload it
                if 'main' in sys.modules:
                    del sys.modules['main']
                import main
            except ImportError:
                # If main.py doesn't exist, maybe it's simple mode?
                # In simple mode, the code is already in globals().
                # But for the guard exercise, we MUST be in project mode to test it properly.
                # However, if it's simple mode, the user's code RAN before the test.
                # We can't catch those prints retrospectively easily.
                # SO: We'll force this exercise to only pass if it can be imported cleanly.
                print("❌_FAIL: Could not find 'main.py'. This exercise requires Project Mode view.")
                return
            except Exception as e:
                print(f"❌_FAIL: Unexpected error: {str(e)}")
                return
        
        output = f.getvalue().strip()
        if output:
            print(f"❌_FAIL: The script printed output during import: '{output}'. You must wrap your tests in 'if __name__ == \"__main__\":' to prevent this.")
            return
            
        # 2. Check if the function exists and works
        if not hasattr(main, 'double'):
            print("❌_FAIL: Function 'double' not found in main.py")
            return
            
        if main.double(10) != 20:
            print("❌_FAIL: Function 'double' is not implemented correctly.")
            return

        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: Internal test error: {str(e)}")

if __name__ == "__main__":
    test()
