
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
    eq(out(s.reverseKGroup(head=mk([1, 2, 3, 4, 5, 6],mod), k=3)), [3, 2, 1, 6, 5, 4])
    eq(out(s.reverseKGroup(head=mk([1, 2, 3, 4, 5],mod), k=3)), [3, 2, 1, 4, 5])
    eq(out(s.reverseKGroup(head=mk([1, 2],mod), k=1)), [1, 2])
