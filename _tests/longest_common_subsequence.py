
def check(mod, eq):
    s = mod.Solution()
    eq(s.longestCommonSubsequence(text1="cat", text2="crabt"), 3)
    eq(s.longestCommonSubsequence(text1="abc", text2="abc"), 3)
    eq(s.longestCommonSubsequence(text1="abc", text2="def"), 0)
