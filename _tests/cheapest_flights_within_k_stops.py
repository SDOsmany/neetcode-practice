
def check(mod, eq):
    s = mod.Solution()
    eq(s.findCheapestPrice(n=4, flights=[[0, 1, 200], [1, 2, 100], [1, 3, 300], [2, 3, 100]], src=0, dst=3, k=1), 500)
    eq(s.findCheapestPrice(n=3, flights=[[1, 0, 100], [1, 2, 200], [0, 2, 100]], src=1, dst=2, k=1), 200)
    eq(s.findCheapestPrice(n=3, flights=[[0, 1, 100]], src=0, dst=2, k=5), -1)
