
def check(mod, eq):
    s = mod.Solution()
    eq(s.checkValidString(s="((**)"), True)
    eq(s.checkValidString(s="(((*)"), False)
    eq(s.checkValidString(s="*)"), True)
    eq(s.checkValidString(s=")*"), False)
