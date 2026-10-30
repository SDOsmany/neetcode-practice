
def check(mod, eq):
    s = mod.Solution()
    eq(s.swimInWater(grid=[[0, 1], [2, 3]]), 3)
    eq(s.swimInWater(grid=[[0, 1, 2, 10], [9, 14, 4, 13], [12, 3, 8, 15], [11, 5, 7, 6]]), 8)
    eq(s.swimInWater(grid=[[0]]), 0)
