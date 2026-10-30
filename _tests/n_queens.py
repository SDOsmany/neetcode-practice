
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(r)
    eq(norm(s.solveNQueens(n=4)), norm([[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]))
    eq(norm(s.solveNQueens(n=1)), norm([["Q"]]))
    eq(norm(s.solveNQueens(n=2)), norm([]))
