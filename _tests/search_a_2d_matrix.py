
def check(mod, eq):
    s = mod.Solution()
    eq(s.searchMatrix(matrix=[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target=10), True)
    eq(s.searchMatrix(matrix=[[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target=15), False)
    eq(s.searchMatrix(matrix=[[5]], target=5), True)
