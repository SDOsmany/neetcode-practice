
def check(mod, eq):
    s = mod.Solution()
    eq(s.networkDelayTime(times=[[1, 2, 1], [2, 3, 1], [1, 4, 4], [3, 4, 1]], n=4, k=1), 3)
    eq(s.networkDelayTime(times=[[1, 2, 1], [2, 3, 1]], n=3, k=2), -1)
    eq(s.networkDelayTime(times=[[1, 2, 5]], n=2, k=1), 5)
