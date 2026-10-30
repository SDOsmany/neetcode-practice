
def check(mod, eq):
    s = mod.Solution()
    eq(s.reverseBits(n=43261596), 964176192)
    eq(s.reverseBits(n=1), 2147483648)
    eq(s.reverseBits(n=4294967295), 4294967295)
