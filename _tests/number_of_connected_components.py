
def check(mod, eq):
    s = mod.Solution()
    eq(s.countComponents(n=3, edges=[[0, 1], [0, 2]]), 1)
    eq(s.countComponents(n=6, edges=[[0, 1], [1, 2], [2, 3], [4, 5]]), 2)
    eq(s.countComponents(n=3, edges=[]), 3)
