
def check(mod, eq):
    s = mod.Solution()
    eq(s.search([3,4,5,6,1,2],1), 4)
    eq(s.search([3,5,6,0,1,2],4), -1)
    eq(s.search([1],1), 0)
    eq(s.search([4,5,6,7,0,1,2],0), 4)
    eq(s.search([5,1,3],5), 0)
