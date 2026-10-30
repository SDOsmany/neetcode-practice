
def check(mod, eq):
    s = mod.Solution()
    eq(s.wordBreak(s="neetcode", wordDict=["neet", "code"]), True)
    eq(s.wordBreak(s="applepenapple", wordDict=["apple", "pen"]), True)
    eq(s.wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]), False)
