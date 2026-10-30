
def check(mod, eq):
    s = mod.Solution()
    eq(s.twoSum([1,2,3,4], 3), [1,2])
    eq(s.twoSum([2,7,11,15], 9), [1,2])
    eq(s.twoSum([-3,-1,0,5], 4), [2,4])
    eq(s.twoSum([1,3,4,5,7,11], 9), [3,4])
