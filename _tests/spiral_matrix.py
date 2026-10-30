
def check(mod, eq):
    s = mod.Solution()
    eq(s.spiralOrder(matrix=[[1, 2], [3, 4]]), [1, 2, 4, 3])
    eq(s.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5])
    eq(s.spiralOrder(matrix=[[1, 2, 3, 4]]), [1, 2, 3, 4])
    eq(s.spiralOrder(matrix=[[1], [2], [3]]), [1, 2, 3])
