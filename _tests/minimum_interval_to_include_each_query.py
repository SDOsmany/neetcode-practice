
def check(mod, eq):
    s = mod.Solution()
    eq(s.minInterval(intervals=[[1, 3], [2, 3], [3, 7], [6, 6]], queries=[2, 3, 1, 7, 6, 8]), [2, 2, 3, 5, 1, -1])
    eq(s.minInterval(intervals=[[1, 4]], queries=[5]), [-1])
    eq(s.minInterval(intervals=[[1, 4], [2, 4]], queries=[3, 3]), [3, 3])
