
def check(mod, eq):
    t = mod.TimeMap()
    t.set("alice","happy",1)
    eq(t.get("alice",1), "happy")
    eq(t.get("alice",2), "happy")
    t.set("alice","sad",3)
    eq(t.get("alice",3), "sad")
    eq(t.get("alice",2), "happy")
    eq(t.get("alice",0), "")
    eq(t.get("bob",5), "")
