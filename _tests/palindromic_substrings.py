
def check(mod, eq):
    s = mod.Solution()
    eq(s.countSubstrings(s="abc"), 3)
    eq(s.countSubstrings(s="aaa"), 6)
    eq(s.countSubstrings(s="abba"), 6)
