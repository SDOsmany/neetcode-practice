
def check(mod, eq):
    s = mod.Solution()
    eq(s.trap(height=[0, 2, 0, 3, 1, 0, 1, 3, 2, 1]), 9)
    eq(s.trap(height=[3, 0, 2]), 2)
    eq(s.trap(height=[1, 2, 3]), 0)
