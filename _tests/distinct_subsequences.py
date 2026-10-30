
def check(mod, eq):
    s = mod.Solution()
    eq(s.numDistinct(s="caaat", t="cat"), 3)
    eq(s.numDistinct(s="xxyxy", t="xy"), 5)
    eq(s.numDistinct(s="abc", t="d"), 0)
