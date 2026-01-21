import os
import subprocess
import sys

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
        
        # Default state utility just returns the string as is, so output would be:
        #   ALICE  
        #   bob 
        # (or similar)
        
        # We expect cleaned names: "alice" and "bob"
        if "alice" in output and "bob" in output and "  " not in output:
             # Further check: should be lowercase
             if output.lower() == output:
                print("✅_PASS_✅")
                return
             else:
                print(f"❌_FAIL: Output should be lowercase. Got: {output}")
        else:
            print(f"❌_FAIL: Expected cleaned names 'alice' and 'bob' without extra spaces. Got: {output}")

    except Exception as e:
        print(f"❌_FAIL: {str(e)}")

if __name__ == "__main__":
    test()
