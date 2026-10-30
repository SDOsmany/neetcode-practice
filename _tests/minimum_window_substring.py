
def check(mod, eq):
    s = mod.Solution()
    eq(s.minWindow(s="OUZODYXAZV", t="XYZ"), "YXAZ")
    eq(s.minWindow(s="xyz", t="xyz"), "xyz")
    eq(s.minWindow(s="x", t="xy"), "")
    eq(s.minWindow(s="aa", t="aa"), "aa")
