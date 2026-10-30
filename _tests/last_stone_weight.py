
def check(mod, eq):
    s = mod.Solution()
    eq(s.lastStoneWeight([2,3,6,2,4]), 1)
    eq(s.lastStoneWeight([1,2]), 1)
    eq(s.lastStoneWeight([5,5]), 0)
    eq(s.lastStoneWeight([9]), 9)
