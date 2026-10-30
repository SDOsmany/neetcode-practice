
def mk(vals, mod):
    head = None
    for v in reversed(vals):
        head = mod.ListNode(v, head)
    return head
def out(n):
    r = []
    while n:
        r.append(n.val)
        n = n.next
    return r

def check(mod, eq):
    s = mod.Solution()
    m = lambda ls: out(s.mergeKLists([mk(x, mod) for x in ls]))
    eq(m([[1,2,4],[1,3,5],[3,6]]), [1,1,2,3,3,4,5,6])
    eq(m([]), [])
    eq(m([[]]), [])
    eq(m([[],[2],[1]]), [1,2])
