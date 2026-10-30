
def check(mod, eq):
    s = mod.Solution()
    eq(s.insert(intervals=[[1, 3], [4, 6]], newInterval=[2, 5]), [[1, 6]])
    eq(s.insert(intervals=[[1, 2], [3, 5], [9, 10]], newInterval=[6, 7]), [[1, 2], [3, 5], [6, 7], [9, 10]])
    eq(s.insert(intervals=[], newInterval=[1, 2]), [[1, 2]])
