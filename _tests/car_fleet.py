
def check(mod, eq):
    s = mod.Solution()
    eq(s.carFleet(target=10, position=[1, 4], speed=[3, 2]), 1)
    eq(s.carFleet(target=10, position=[4, 1, 0, 7], speed=[2, 2, 1, 1]), 3)
    eq(s.carFleet(target=12, position=[3], speed=[3]), 1)
