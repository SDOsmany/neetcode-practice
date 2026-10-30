
def check(mod, eq):
    s = mod.Solution()
    eq(s.rob(nums=[3, 4, 3]), 4)
    eq(s.rob(nums=[2, 9, 8, 3, 6]), 15)
    eq(s.rob(nums=[7]), 7)
