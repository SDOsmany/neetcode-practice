
def check(mod, eq):
    s = mod.Solution()
    eq(s.isValid("[]"), True)
    eq(s.isValid("([{}])"), True)
    eq(s.isValid("[(])"), False)
    eq(s.isValid("("), False)
    eq(s.isValid(")"), False)
