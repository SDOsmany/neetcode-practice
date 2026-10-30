
def check(mod, eq):
    s = mod.Solution()
    eq(sorted(s.kClosest([[0,2],[2,2]],1)), [[0,2]])
    eq(sorted(s.kClosest([[0,2],[2,0],[2,2]],2)), [[0,2],[2,0]])
    eq(sorted(s.kClosest([[3,3],[5,-1],[-2,4]],2)), [[-2,4],[3,3]])
