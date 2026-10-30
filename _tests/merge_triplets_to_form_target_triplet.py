
def check(mod, eq):
    s = mod.Solution()
    eq(s.mergeTriplets(triplets=[[1, 2, 3], [7, 1, 1]], target=[7, 2, 3]), True)
    eq(s.mergeTriplets(triplets=[[2, 5, 6], [1, 4, 4], [5, 7, 5]], target=[5, 4, 6]), False)
    eq(s.mergeTriplets(triplets=[[1, 1, 1]], target=[1, 1, 1]), True)
