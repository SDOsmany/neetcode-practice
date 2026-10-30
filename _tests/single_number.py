
def check(mod, eq):
    s = mod.Solution()
    eq(s.singleNumber(nums=[3, 2, 3]), 2)
    eq(s.singleNumber(nums=[7, 6, 6, 7, 8]), 8)
    eq(s.singleNumber(nums=[-1]), -1)
