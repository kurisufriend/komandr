depends = ["bprint", "test_lib"]
def run(l):
    if "test_lib" not in l.keys(): print("requires test_lib library!");return
    l["bprint"].p(f"printing out the test value woot woot: {l['test_lib'].test_var}")
    l["bprint"].p("callign the test function woot woot")
    l["test_lib"].test_func()