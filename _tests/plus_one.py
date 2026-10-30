
def check(mod, eq):
    s = mod.Solution()
    eq(s.plusOne(digits=[1, 2, 3, 4]), [1, 2, 3, 5])
    eq(s.plusOne(digits=[9, 9, 9]), [1, 0, 0, 0])
    eq(s.plusOne(digits=[0]), [1])
