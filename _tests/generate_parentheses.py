
def check(mod, eq):
    s = mod.Solution()
    eq(sorted(s.generateParenthesis(3)), ["((()))","(()())","(())()","()(())","()()()"])
    eq(s.generateParenthesis(1), ["()"])
    eq(len(s.generateParenthesis(4)), 14)
