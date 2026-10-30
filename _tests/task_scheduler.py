
def check(mod, eq):
    s = mod.Solution()
    eq(s.leastInterval(tasks=["X", "X", "Y", "Y"], n=2), 5)
    eq(s.leastInterval(tasks=["A", "A", "A", "B", "C"], n=3), 9)
    eq(s.leastInterval(tasks=["A", "B", "C"], n=5), 3)
