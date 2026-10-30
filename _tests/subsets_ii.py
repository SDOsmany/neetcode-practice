
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.subsetsWithDup(nums=[1, 2, 1])), norm([[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]))
    eq(norm(s.subsetsWithDup(nums=[7, 7])), norm([[], [7], [7, 7]]))
