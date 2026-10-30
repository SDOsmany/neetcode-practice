
def check(mod, eq):
    s = mod.Solution()
    eq(s.coinChange(coins=[1, 5, 10], amount=12), 3)
    eq(s.coinChange(coins=[2], amount=3), -1)
    eq(s.coinChange(coins=[1], amount=0), 0)
    eq(s.coinChange(coins=[1, 3, 4], amount=6), 2)
