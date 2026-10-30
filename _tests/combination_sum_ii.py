
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.combinationSum2(candidates=[9, 2, 2, 4, 6, 1, 5], target=8)), norm([[1, 2, 5], [2, 2, 4], [2, 6]]))
    eq(norm(s.combinationSum2(candidates=[1, 2, 3, 4, 5], target=7)), norm([[1, 2, 4], [2, 5], [3, 4]]))
    eq(norm(s.combinationSum2(candidates=[3], target=1)), norm([]))
