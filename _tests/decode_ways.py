
def check(mod, eq):
    s = mod.Solution()
    eq(s.numDecodings(s="12"), 2)
    eq(s.numDecodings(s="226"), 3)
    eq(s.numDecodings(s="01"), 0)
    eq(s.numDecodings(s="10"), 1)
