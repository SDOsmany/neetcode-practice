
def check(mod, eq):
    s = mod.Solution()
    a = [[1, 2], [3, 4]]
    s.rotate(matrix=a)
    eq(a, [[3, 1], [4, 2]])
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(matrix=a)
    eq(a, [[7, 4, 1], [8, 5, 2], [9, 6, 3]])
