
def check(mod, eq):
    s = mod.Solution()
    eq(s.hammingWeight(n=23), 4)
    eq(s.hammingWeight(n=2147483645), 30)
    eq(s.hammingWeight(n=0), 0)
