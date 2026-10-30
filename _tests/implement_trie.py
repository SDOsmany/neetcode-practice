
def check(mod, eq):
    t = mod.PrefixTree()
    t.insert("dog")
    eq(t.search("dog"), True)
    eq(t.search("do"), False)
    eq(t.startsWith("do"), True)
    eq(t.startsWith("cat"), False)
    t.insert("do")
    eq(t.search("do"), True)
