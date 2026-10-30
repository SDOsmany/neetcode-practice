
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxSubArray([2,-3,4,-2,2,1,-1,4]), 8)
    eq(s.maxSubArray([-1]), -1)
    eq(s.maxSubArray([-3,-2,-5]), -2)
    eq(s.maxSubArray([1,2,3]), 6)
