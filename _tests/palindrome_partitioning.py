
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(r)
    eq(norm(s.partition(s="aab")), norm([["a", "a", "b"], ["aa", "b"]]))
    eq(norm(s.partition(s="a")), norm([["a"]]))
    eq(norm(s.partition(s="aba")), norm([["a", "b", "a"], ["aba"]]))
