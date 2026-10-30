
def check(mod, eq):
    s = mod.Solution()
    eq(s.characterReplacement(s="XYYX", k=2), 4)
    eq(s.characterReplacement(s="AAABABB", k=1), 5)
    eq(s.characterReplacement(s="A", k=0), 1)
