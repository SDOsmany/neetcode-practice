
def check(mod, eq):
    s = mod.Solution()
    eq(s.search([-1,0,2,4,6,8],4), 3)
    eq(s.search([-1,0,2,4,6,8],3), -1)
    eq(s.search([5],5), 0)
    eq(s.search([],1), -1)
    eq(s.search([1,2],2), 1)
