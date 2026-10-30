
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
    a = mk([2, 4, 6, 8],mod)
    s.reorderList(head=a)
    eq(out(a), [2, 8, 4, 6])
    a = mk([2, 4, 6, 8, 10],mod)
    s.reorderList(head=a)
    eq(out(a), [2, 10, 4, 8, 6])
    a = mk([1, 2],mod)
    s.reorderList(head=a)
    eq(out(a), [1, 2])
