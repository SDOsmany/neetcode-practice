
def check(mod, eq):
    s = mod.Solution()
    eq(s.findTargetSumWays(nums=[2, 2, 2], target=2), 3)
    eq(s.findTargetSumWays(nums=[1], target=2), 0)
    eq(s.findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3), 5)
