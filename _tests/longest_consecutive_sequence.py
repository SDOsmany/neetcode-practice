
def check(mod, eq):
    s = mod.Solution()
    eq(s.longestConsecutive(nums=[2, 20, 4, 10, 3, 4, 5]), 4)
    eq(s.longestConsecutive(nums=[0, 3, 2, 5, 4, 6, 1, 1]), 7)
    eq(s.longestConsecutive(nums=[]), 0)
