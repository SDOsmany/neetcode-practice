
def check(mod, eq):
    s = mod.Solution()
    eq(s.longestIncreasingPath(matrix=[[5, 5, 3], [2, 3, 6], [1, 1, 1]]), 4)
    eq(s.longestIncreasingPath(matrix=[[1, 2, 3], [2, 1, 4], [7, 6, 5]]), 7)
    eq(s.longestIncreasingPath(matrix=[[1]]), 1)
