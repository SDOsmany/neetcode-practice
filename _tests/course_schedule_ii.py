
def check(mod, eq):
    s = mod.Solution()
    def valid(n, pre):
        order = s.findOrder(n, pre)
        pos = {c: i for i, c in enumerate(order)}
        return sorted(order) == list(range(n)) and all(pos[b] < pos[a] for a, b in pre)
    eq(valid(3, [[1,0]]), True)
    eq(valid(4, [[1,0],[2,0],[3,1],[3,2]]), True)
    eq(valid(1, []), True)
    eq(s.findOrder(2, [[0,1],[1,0]]), [])
