
def check(mod, eq):
    s = mod.Solution()
    eq(s.minEatingSpeed([1,4,3,2],9), 2)
    eq(s.minEatingSpeed([25,10,23,4],4), 25)
    eq(s.minEatingSpeed([3,6,7,11],8), 4)
    eq(s.minEatingSpeed([30,11,23,4,20],6), 23)
