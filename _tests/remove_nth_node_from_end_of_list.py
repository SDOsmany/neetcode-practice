
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
    eq(out(s.removeNthFromEnd(head=mk([1, 2, 3, 4],mod), n=2)), [1, 2, 4])
    eq(out(s.removeNthFromEnd(head=mk([5],mod), n=1)), [])
    eq(out(s.removeNthFromEnd(head=mk([1, 2],mod), n=2)), [2])
