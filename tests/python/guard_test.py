import io
from contextlib import redirect_stdout

def test():
    try:
        # We want to check if importing the file produces output.
        # It shouldn't, if the user used if __name__ == "__main__":
        
        f = io.StringIO()
        with redirect_stdout(f):
            try:
                import solution # Users code usually injected as whole
            except ImportError:
                # If we are in project mode it might be named something else
                # But here we just assume the code is at top level
                pass
        
        output = f.getvalue().strip()
        if output:
            print(f"❌_FAIL: Script printed output during import: '{output}'. Use if __name__ == '__main__': to guard it.")
            return
            
        print("✅_PASS_✅")
    except Exception as e:
        print(f"❌_FAIL: {str(e)}")

if __name__ == "__main__":
    test()
