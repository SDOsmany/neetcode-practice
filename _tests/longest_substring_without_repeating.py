
def check(mod, eq):
    s = mod.Solution()
    eq(s.lengthOfLongestSubstring("zxyzxyz"), 3)
    eq(s.lengthOfLongestSubstring("xxxx"), 1)
    eq(s.lengthOfLongestSubstring(""), 0)
    eq(s.lengthOfLongestSubstring("abba"), 2)
    eq(s.lengthOfLongestSubstring("dvdf"), 3)
