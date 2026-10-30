
def check(mod, eq):
    s = mod.Solution()
    eq(s.isInterleave(s1="aaaa", s2="bbbb", s3="aabbbbaa"), True)
    eq(s.isInterleave(s1="abc", s2="xyz", s3="abxzcy"), False)
    eq(s.isInterleave(s1="", s2="", s3=""), True)
    eq(s.isInterleave(s1="a", s2="b", s3="abc"), False)
