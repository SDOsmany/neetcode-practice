
def check(mod, eq):
    s = mod.Solution()
    eq(s.hasDuplicate([1,2,3,1]), True)
    eq(s.hasDuplicate([1,2,3,4]), False)
    eq(s.hasDuplicate([]), False)
    eq(s.hasDuplicate([7,7]), True)
