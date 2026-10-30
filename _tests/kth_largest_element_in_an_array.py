
def check(mod, eq):
    s = mod.Solution()
    eq(s.findKthLargest(nums=[2, 3, 1, 5, 4], k=2), 4)
    eq(s.findKthLargest(nums=[2, 3, 1, 1, 5, 5, 4], k=3), 4)
    eq(s.findKthLargest(nums=[1], k=1), 1)
