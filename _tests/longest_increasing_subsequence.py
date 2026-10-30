
def check(mod, eq):
    s = mod.Solution()
    eq(s.lengthOfLIS(nums=[9, 1, 4, 2, 3, 3, 7]), 4)
    eq(s.lengthOfLIS(nums=[0, 3, 1, 3, 2, 3]), 4)
    eq(s.lengthOfLIS(nums=[5, 5, 5]), 1)
