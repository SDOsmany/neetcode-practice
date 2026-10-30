
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxAreaOfIsland(grid=[[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]), 6)
    eq(s.maxAreaOfIsland(grid=[[0, 0]]), 0)
    eq(s.maxAreaOfIsland(grid=[[1]]), 1)
