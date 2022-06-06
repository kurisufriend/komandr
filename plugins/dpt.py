depends = ["bprint", "meido"]
def run(l):
    l["bprint"].p(f"found {len(l['meido'].instance.get_boards())} boards")