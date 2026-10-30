
def check(mod, eq):
    s = mod.Solution()
    eq(s.productExceptSelf(nums=[1, 2, 4, 6]), [48, 24, 12, 8])
    eq(s.productExceptSelf(nums=[-1, 0, 1, 2, 3]), [0, -6, 0, 0, 0])
    eq(s.productExceptSelf(nums=[2, 3]), [3, 2])
