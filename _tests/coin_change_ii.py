
def check(mod, eq):
    s = mod.Solution()
    eq(s.change(amount=4, coins=[1, 2, 3]), 4)
    eq(s.change(amount=3, coins=[2]), 0)
    eq(s.change(amount=0, coins=[5]), 1)
