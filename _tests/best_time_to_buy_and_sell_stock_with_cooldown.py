
def check(mod, eq):
    s = mod.Solution()
    eq(s.maxProfit(prices=[1, 3, 4, 0, 4]), 6)
    eq(s.maxProfit(prices=[1]), 0)
    eq(s.maxProfit(prices=[1, 2, 3, 0, 2]), 3)
