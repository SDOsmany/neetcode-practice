
def check(mod, eq):
    s = mod.Solution()
    eq(s.getSum(a=1, b=1), 2)
    eq(s.getSum(a=4, b=7), 11)
    eq(s.getSum(a=-2, b=3), 1)
    eq(s.getSum(a=-5, b=-6), -11)
