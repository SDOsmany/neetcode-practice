
def check(mod, eq):
    s = mod.Solution()
    eq(s.isPalindrome("Was it a car or a cat I saw?"), True)
    eq(s.isPalindrome("tab a cat"), False)
    eq(s.isPalindrome(" "), True)
    eq(s.isPalindrome("0P"), False)
