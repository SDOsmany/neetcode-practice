
def check(mod, eq):
    s = mod.Solution()
    a = [[0, 1], [1, 1]]
    s.setZeroes(matrix=a)
    eq(a, [[0, 0], [0, 1]])
    a = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
    s.setZeroes(matrix=a)
    eq(a, [[1, 0, 3], [0, 0, 0], [6, 0, 8]])
    a = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(matrix=a)
    eq(a, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]])
