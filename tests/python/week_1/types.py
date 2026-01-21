import inspect
from typing import List, Callable
try:
    sig = inspect.signature(process_items)
    
    # 1. Check 'items' (Should be List)
    t_items = sig.parameters['items'].annotation
    assert t_items != inspect._empty, "Missing type hint for 'items'"
    assert "List" in str(t_items) or "list" in str(t_items), f"'items' should be a List, not {t_items}"

    # 2. Check 'transformer' (Should be Callable)
    t_trans = sig.parameters['transformer'].annotation
    assert t_trans != inspect._empty, "Missing type hint for 'transformer'"
    assert "Callable" in str(t_trans) or "callable" in str(t_trans), f"'transformer' should be a Callable, not {t_trans}"

    # 3. Check Return Type (Should be List)
    t_ret = sig.return_annotation
    assert t_ret != inspect._empty, "Missing return type hint"
    assert "List" in str(t_ret) or "list" in str(t_ret), f"Return type should be a List, not {t_ret}"
    
    # 4. Logic check
    assert process_items([1,2], lambda x: x*2) == [2,4]
    print("✅_PASS_✅")
except Exception as e:
    print(f"❌_FAIL: {e}")
