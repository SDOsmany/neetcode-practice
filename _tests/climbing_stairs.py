
def check(mod, eq):
    s = mod.Solution()
    eq(s.climbStairs(1), 1)
    eq(s.climbStairs(2), 2)
    eq(s.climbStairs(3), 3)
    eq(s.climbStairs(10), 89)
    eq(s.climbStairs(40), 165580141)
