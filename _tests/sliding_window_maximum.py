
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxSlidingWindow(nums=[1, 2, 1, 0, 4, 2, 6], k=3), [2, 2, 4, 4, 6])
    eq(s.maxSlidingWindow(nums=[5], k=1), [5])
    eq(s.maxSlidingWindow(nums=[9, 8, 7], k=2), [9, 8])
