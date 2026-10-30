
def check(mod, eq):
    s = mod.Solution()
    eq(s.reverse(x=1234), 4321)
    eq(s.reverse(x=-1234), -4321)
    eq(s.reverse(x=120), 21)
    eq(s.reverse(x=1534236469), 0)
