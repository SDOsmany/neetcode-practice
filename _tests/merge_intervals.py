
def check(mod, eq):
    s = mod.Solution()
    eq(s.merge(intervals=[[1, 3], [1, 5], [6, 7]]), [[1, 5], [6, 7]])
    eq(s.merge(intervals=[[1, 2], [2, 3]]), [[1, 3]])
    eq(s.merge(intervals=[[4, 5], [1, 2]]), [[1, 2], [4, 5]])
