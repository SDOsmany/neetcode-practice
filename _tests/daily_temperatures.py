
def check(mod, eq):
    s = mod.Solution()
    eq(s.dailyTemperatures([30,38,30,36,35,40,28]), [1,4,1,2,1,0,0])
    eq(s.dailyTemperatures([22,21,20]), [0,0,0])
    eq(s.dailyTemperatures([1,2,3]), [1,1,0])
