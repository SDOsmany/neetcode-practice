
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(sorted(x) for x in r)
    eq(norm(s.subsets([1,2,3])), [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])
    eq(norm(s.subsets([7])), [[],[7]])
