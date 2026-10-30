
def check(mod, eq):
    s = mod.Solution()
    eq(s.canPartition(nums=[1, 2, 3, 4]), True)
    eq(s.canPartition(nums=[1, 2, 3, 4, 5]), False)
    eq(s.canPartition(nums=[1, 2, 5]), False)
