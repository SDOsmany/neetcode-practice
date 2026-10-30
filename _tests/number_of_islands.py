
def check(mod, eq):
    s = mod.Solution()
    eq(s.numIslands([["1","1","0"],["0","1","0"],["0","0","1"]]), 2)
    eq(s.numIslands([["0"]]), 0)
    eq(s.numIslands([["1","1"],["1","1"]]), 1)
    eq(s.numIslands([["1","0","1"],["0","1","0"],["1","0","1"]]), 5)
