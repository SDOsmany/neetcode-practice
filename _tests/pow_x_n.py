
def check(mod, eq):
    s = mod.Solution()
    eq(s.myPow(2.0, 5), 32.0)
    eq(round(s.myPow(1.1, 10), 5), 2.59374)
    eq(s.myPow(2.0, -3), 0.125)
    eq(s.myPow(5.0, 0), 1.0)
    eq(s.myPow(1.0, 1000000), 1.0)
