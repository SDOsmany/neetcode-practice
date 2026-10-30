
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
    h = mk([1,2,3,4],mod); h.next.next.next.next = h.next
    eq(s.hasCycle(h), True)
    eq(s.hasCycle(mk([1,2],mod)), False)
    eq(s.hasCycle(None), False)
    h = mk([1],mod); h.next = h
    eq(s.hasCycle(h), True)
