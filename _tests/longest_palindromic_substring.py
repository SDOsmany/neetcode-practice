
def check(mod, eq):
    s = mod.Solution()
    eq(s.longestPalindrome("ababd") in ("bab","aba"), True)
    eq(s.longestPalindrome("abbc"), "bb")
    eq(s.longestPalindrome("x"), "x")
    eq(s.longestPalindrome("forgeeksskeegfor"), "geeksskeeg")
