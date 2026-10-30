
def check(mod, eq):
    s = mod.Solution()
    eq(s.canJump([1,2,0,1,0]), True)
    eq(s.canJump([1,2,1,0,1]), False)
    eq(s.canJump([0]), True)
    eq(s.canJump([2,0,0]), True)
