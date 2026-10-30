
def check(mod, eq):
    s = mod.Solution()
    eq(s.multiply("3","4"), "12")
    eq(s.multiply("111","222"), "24642")
    eq(s.multiply("0","999"), "0")
    eq(s.multiply("123456789","987654321"), "121932631112635269")
