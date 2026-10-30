
def check(mod, eq):
    s = mod.Solution()
    a, b, c = mod.Node(1), mod.Node(2), mod.Node(3)
    a.neighbors = [b]; b.neighbors = [a, c]; c.neighbors = [b]
    x = s.cloneGraph(a)
    eq(x is not None and x is not a, True)
    eq(x.val, 1)
    y = x.neighbors[0]
    eq(y is not b and y.val == 2, True)
    eq(sorted(n.val for n in y.neighbors), [1, 3])
    eq(y.neighbors[0] is x or y.neighbors[1] is x, True)
    eq(s.cloneGraph(None), None)
    n = mod.Node(5)
    eq(s.cloneGraph(n).neighbors, [])
