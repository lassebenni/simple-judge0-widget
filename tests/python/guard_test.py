import io
import sys
from contextlib import redirect_stdout

def test():
    try:
        # Capture output during import
        f = io.StringIO()
        with redirect_stdout(f):
            try:
                # In our Project Mode, the user's main file is always 'main.py'
                import main
            except ImportError:
                # If we are in simple mode (appending), 'main' won't exist as a separate module
                # In that case, the naked prints will have ALREADY executed.
                # But notice: the 'main_guard' exercise is best tested in Project Mode.
                # However, we can try to find if 'double' is in globals and if output was already produced
                print("❌_FAIL: Could not import 'main.py'. Are you in Project Mode?")
                return
        
        output = f.getvalue().strip()
        if output:
            print(f"❌_FAIL: Script printed output during import: '{output}'. Use 'if __name__ == \"__main__\":' to guard your prints.")
            return
            
        # Also check if the function exists
        if not hasattr(main, 'double'):
            print("❌_FAIL: Function 'double' not found in main.py")
            return

        if main.double(10) != 20:
             print("❌_FAIL: Function 'double' does not work correctly.")
             return

        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: {str(e)}")

if __name__ == "__main__":
    test()
