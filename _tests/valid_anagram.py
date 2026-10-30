
def check(mod, eq):
    s = mod.Solution()
    eq(s.isAnagram(s="racecar", t="carrace"), True)
    eq(s.isAnagram(s="jar", t="jam"), False)
    eq(s.isAnagram(s="ab", t="abb"), False)
