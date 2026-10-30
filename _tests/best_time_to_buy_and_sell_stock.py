
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxProfit([10,1,5,6,7,1]), 6)
    eq(s.maxProfit([10,8,7,5,2]), 0)
    eq(s.maxProfit([1]), 0)
    eq(s.maxProfit([2,4,1,3]), 2)
