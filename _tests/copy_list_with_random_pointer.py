
def check(mod, eq):
    s = mod.Solution()
    a, b, c = mod.Node(3), mod.Node(7), mod.Node(1)
    a.next = b; b.next = c; a.random = c; c.random = a; b.random = b
    x = s.copyRandomList(a)
    eq(x is not None and x is not a, True)
    eq([x.val, x.next.val, x.next.next.val], [3, 7, 1])
    eq(x.random is x.next.next, True)
    eq(x.next.random is x.next, True)
    eq(x.next.next.random is x, True)
    eq(x.next is not b, True)
    eq(s.copyRandomList(None), None)
