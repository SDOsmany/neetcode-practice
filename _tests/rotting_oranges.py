
def check(mod, eq):
    s = mod.Solution()
    eq(s.orangesRotting([[1,1,0],[0,1,1],[0,1,2]]), 4)
    eq(s.orangesRotting([[1,0,1],[0,2,0],[1,0,1]]), -1)
    eq(s.orangesRotting([[0]]), 0)
    eq(s.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
