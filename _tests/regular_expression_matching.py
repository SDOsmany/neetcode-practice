
def check(mod, eq):
    s = mod.Solution()
    eq(s.isMatch(s="aa", p=".b"), False)
    eq(s.isMatch(s="nnn", p="n*"), True)
    eq(s.isMatch(s="nb", p=".*b"), True)
    eq(s.isMatch(s="aab", p="c*a*b"), True)
    eq(s.isMatch(s="ab", p="a"), False)
