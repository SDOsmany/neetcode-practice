
def check(mod, eq):
    d = mod.DetectSquares()
    d.add([1,1]); d.add([2,2]); d.add([1,2])
    eq(d.count([2,1]), 1)
    eq(d.count([3,3]), 0)
    d.add([2,2])
    eq(d.count([2,1]), 2)
