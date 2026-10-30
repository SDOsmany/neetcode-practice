
def check(mod, eq):
    s = mod.Solution()
    eq(s.evalRPN(tokens=["1", "2", "+", "3", "*", "4", "-"]), 5)
    eq(s.evalRPN(tokens=["6", "-4", "/"]), -1)
    eq(s.evalRPN(tokens=["7"]), 7)
