
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxArea([1,7,2,5,4,7,3,6]), 36)
    eq(s.maxArea([2,2,2]), 4)
    eq(s.maxArea([1,1]), 1)
    eq(s.maxArea([1,8,6,2,5,4,8,3,7]), 49)
