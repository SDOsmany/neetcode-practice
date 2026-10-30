
def check(mod, eq):
    s = mod.Solution()
    eq(s.findMin(nums=[3, 4, 5, 6, 1, 2]), 1)
    eq(s.findMin(nums=[4, 5, 0, 1, 2, 3]), 0)
    eq(s.findMin(nums=[4, 5, 6, 7]), 4)
