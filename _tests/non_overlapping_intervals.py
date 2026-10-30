
def check(mod, eq):
    s = mod.Solution()
    eq(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 4], [1, 4]]), 1)
    eq(s.eraseOverlapIntervals(intervals=[[1, 2], [2, 4]]), 0)
    eq(s.eraseOverlapIntervals(intervals=[[1, 2], [1, 2], [1, 2]]), 2)
