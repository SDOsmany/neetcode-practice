
def check(mod, eq):
    s = mod.Solution()
    eq(s.validTree(n=5, edges=[[0, 1], [0, 2], [0, 3], [1, 4]]), True)
    eq(s.validTree(n=5, edges=[[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]), False)
    eq(s.validTree(n=4, edges=[[0, 1], [2, 3], [1, 0]]), False)
