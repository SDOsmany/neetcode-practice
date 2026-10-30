
def check(mod, eq):
    s = mod.Solution()
    eq(s.countBits(n=4), [0, 1, 1, 2, 1])
    eq(s.countBits(n=0), [0])
    eq(s.countBits(n=7), [0, 1, 1, 2, 1, 2, 2, 3])
