
def check(mod, eq):
    s = mod.Solution()
    eq(s.alienOrder(words=["wrt", "wrf", "er", "ett", "rftt"]), "wertf")
    eq(s.alienOrder(words=["z", "x", "z"]), "")
    eq(s.alienOrder(words=["abc", "ab"]), "")
    eq(s.alienOrder(words=["z", "x"]), "zx")
