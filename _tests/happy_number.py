
def check(mod, eq):
    s = mod.Solution()
    eq(s.isHappy(n=100), True)
    eq(s.isHappy(n=101), False)
    eq(s.isHappy(n=19), True)
