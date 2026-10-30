
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.threeSum(nums=[-1, 0, 1, 2, -1, -4])), norm([[-1, -1, 2], [-1, 0, 1]]))
    eq(norm(s.threeSum(nums=[0, 1, 1])), norm([]))
    eq(norm(s.threeSum(nums=[0, 0, 0, 0])), norm([[0, 0, 0]]))
