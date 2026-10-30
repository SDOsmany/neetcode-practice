
def check(mod, eq):
    s = mod.Solution()
    eq(s.uniquePaths(m=3, n=6), 21)
    eq(s.uniquePaths(m=3, n=3), 6)
    eq(s.uniquePaths(m=1, n=5), 1)
