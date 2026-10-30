
def check(mod, eq):
    s = mod.Solution()
    eq(s.checkInclusion("abc","lecabee"), True)
    eq(s.checkInclusion("abc","lecaabee"), False)
    eq(s.checkInclusion("ab","a"), False)
    eq(s.checkInclusion("adc","dcda"), True)
