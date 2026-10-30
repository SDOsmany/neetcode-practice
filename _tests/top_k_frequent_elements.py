
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted((sorted(x) if isinstance(x, list) else x) for x in r)
    eq(norm(s.topKFrequent(nums=[1, 2, 2, 3, 3, 3], k=2)), norm([2, 3]))
    eq(norm(s.topKFrequent(nums=[7, 7], k=1)), norm([7]))
    eq(norm(s.topKFrequent(nums=[4, 1, 4, 2, 2, 4], k=2)), norm([4, 2]))
