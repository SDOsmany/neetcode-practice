
def check(mod, eq):
    k = mod.KthLargest(3,[1,2,3,3])
    eq([k.add(v) for v in [3,5,6,7,8]], [3,3,3,5,6])
    k = mod.KthLargest(1,[])
    eq([k.add(v) for v in [-3,-2,-4,0,4]], [-3,-2,-2,0,4])
