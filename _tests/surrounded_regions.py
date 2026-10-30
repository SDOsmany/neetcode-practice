
def check(mod, eq):
    s = mod.Solution()
    a = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "O"]]
    s.solve(board=a)
    eq(a, [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "O"]])
    a = [["O", "O"], ["O", "X"]]
    s.solve(board=a)
    eq(a, [["O", "O"], ["O", "X"]])
    a = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
    s.solve(board=a)
    eq(a, [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]])
