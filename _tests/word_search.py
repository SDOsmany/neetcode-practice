
def check(mod, eq):
    s = mod.Solution()
    eq(s.exist(board=[["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], word="CAT"), True)
    eq(s.exist(board=[["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], word="BAT"), False)
    eq(s.exist(board=[["A", "A"]], word="AAA"), False)
