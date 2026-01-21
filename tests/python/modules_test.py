import os
import subprocess

def test():
    try:
        # Check for files
        if not os.path.exists("main.py"):
            print("❌_FAIL: main.py not found.")
            return
        if not os.path.exists("utils.py"):
            print("❌_FAIL: utils.py not found.")
            return

        # Run main.py
        result = subprocess.run([sys.executable, "main.py"], capture_output=True, text=True)
        output = result.stdout.strip()

        # We expect main.py to print the cleaned name
        if "alice" in output.lower() and "bob" in output.lower():
            print("✅_PASS_✅")
        else:
            print(f"❌_FAIL: Output did not contain expected cleaned names 'alice' and 'bob'. Got: {output}")

    except Exception as e:
        print(f"❌_FAIL: {str(e)}")

if __name__ == "__main__":
    import sys
    test()
