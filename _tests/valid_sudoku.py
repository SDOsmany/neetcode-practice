
def check(mod, eq):
    s = mod.Solution()
    def b(*cells):
        g = [["."] * 9 for _ in range(9)]
        for r, c, v in cells:
            g[r][c] = v
        return g
    eq(s.isValidSudoku(b((0,0,"5"),(4,4,"5"))), True)
    eq(s.isValidSudoku(b((0,0,"5"),(1,1,"5"))), False)
    eq(s.isValidSudoku(b((0,0,"7"),(0,8,"7"))), False)
    eq(s.isValidSudoku(b((0,3,"2"),(8,3,"2"))), False)
    eq(s.isValidSudoku(b()), True)
