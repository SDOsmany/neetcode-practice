
def check(mod, eq):
    s = mod.Solution()
    eq(s.twoSum([3,4,5,6], 7), [0,1])
    eq(s.twoSum([4,5,6], 10), [0,2])
    eq(s.twoSum([5,5], 10), [0,1])
    eq(s.twoSum([-1,8,3,-4], -5), [0,3])
