
def check(mod, eq):
    s = mod.Solution()
    norm = lambda r: sorted(sorted(x) for x in r)
    eq(norm(s.combinationSum([2,5,6,9],9)), [[2,2,5],[9]])
    eq(norm(s.combinationSum([3,4,5],16)), [[3,3,3,3,4],[3,3,5,5],[3,4,4,5],[4,4,4,4]])
    eq(norm(s.combinationSum([3],5)), [])
