
def check(mod, eq):
    s = mod.Solution()
    eq(s.minCostConnectPoints(points=[[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]), 10)
    eq(s.minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]), 18)
    eq(s.minCostConnectPoints(points=[[0, 0]]), 0)
