
def check(mod, eq):
    s = mod.Solution()
    eq(s.jump([2,4,1,1,1,1]), 2)
    eq(s.jump([2,1,2,1,0]), 2)
    eq(s.jump([0]), 0)
    eq(s.jump([2,3,1,1,4]), 2)
    eq(s.jump([1,1,1,1]), 3)
