depends = ["bprint", "meido"]
def run(l):
    pages = l['meido'].instance.get_catalog("g")
    for page in pages:
        for thread in page["threads"]:
            if not thread.get("sub"): continue
            if "/dpt/" in thread["sub"]:
                l["sand"].box["dpt"] = thread["no"]
                l["bprint"].p(f"found /dpt/! thread no: {thread['no']}")
