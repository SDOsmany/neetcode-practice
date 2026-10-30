
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(r)
    eq(norm(s.permute(nums=[1, 2, 3])), norm([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]))
    eq(norm(s.permute(nums=[7])), norm([[7]]))
