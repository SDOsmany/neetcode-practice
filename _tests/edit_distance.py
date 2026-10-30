
def check(mod, eq):
    s = mod.Solution()
    eq(s.minDistance(word1="monkeys", word2="money"), 2)
    eq(s.minDistance(word1="neatcdee", word2="neetcode"), 3)
    eq(s.minDistance(word1="", word2="abc"), 3)
