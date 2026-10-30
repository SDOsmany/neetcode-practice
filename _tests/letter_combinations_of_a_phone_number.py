
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.letterCombinations(digits="34")), norm(["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]))
    eq(norm(s.letterCombinations(digits="")), norm([]))
    eq(norm(s.letterCombinations(digits="7")), norm(["p", "q", "r", "s"]))
