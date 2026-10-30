
def check(mod, eq):
    s = mod.Solution()
    eq(s.rob([1,1,3,3]), 4)
    eq(s.rob([2,9,8,3,6]), 16)
    eq(s.rob([]), 0)
    eq(s.rob([5]), 5)
    eq(s.rob([2,1,1,2]), 4)
