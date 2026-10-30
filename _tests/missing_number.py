
def check(mod, eq):
    s = mod.Solution()
    eq(s.missingNumber(nums=[1, 2, 3]), 0)
    eq(s.missingNumber(nums=[0, 2]), 1)
    eq(s.missingNumber(nums=[0, 1]), 2)
