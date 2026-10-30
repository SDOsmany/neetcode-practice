
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.findWords(board=[["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]], words=["bat", "cat", "back", "backend", "stack"])), norm(["cat", "back", "backend"]))
    eq(norm(s.findWords(board=[["x", "o"], ["x", "o"]], words=["xoxo"])), norm([]))
    eq(norm(s.findWords(board=[["a", "a"]], words=["aaa"])), norm([]))
