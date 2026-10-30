
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxCoins(nums=[4, 2, 3, 7]), 143)
    eq(s.maxCoins(nums=[3, 1, 5, 8]), 167)
    eq(s.maxCoins(nums=[5]), 5)
