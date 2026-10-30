
def check(mod, eq):
    s = mod.Solution()
    eq(s.minCostClimbingStairs(cost=[1, 2, 3]), 2)
    eq(s.minCostClimbingStairs(cost=[1, 2, 1, 2, 1, 1, 1]), 4)
    eq(s.minCostClimbingStairs(cost=[5, 5]), 5)
