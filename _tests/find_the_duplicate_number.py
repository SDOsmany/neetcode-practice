
def check(mod, eq):
    s = mod.Solution()
    eq(s.findDuplicate(nums=[1, 2, 3, 2, 2]), 2)
    eq(s.findDuplicate(nums=[1, 2, 3, 4, 4]), 4)
    eq(s.findDuplicate(nums=[3, 1, 3, 4, 2]), 3)
