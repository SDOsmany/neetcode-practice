
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxProduct(nums=[1, 2, -3, 4]), 4)
    eq(s.maxProduct(nums=[-2, -1]), 2)
    eq(s.maxProduct(nums=[-2, 0, -1]), 0)
    eq(s.maxProduct(nums=[2, 3, -2, 4, -1]), 48)
