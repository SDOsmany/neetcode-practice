
def check(mod, eq):
    s = mod.Solution()
    eq(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]), 5)
    eq(s.ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]), 0)
    eq(s.ladderLength(beginWord="a", endWord="c", wordList=["a", "b", "c"]), 2)
