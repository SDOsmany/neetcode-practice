
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
    eq(out(s.addTwoNumbers(l1=mk([1, 2, 3],mod), l2=mk([4, 5, 6],mod))), [5, 7, 9])
    eq(out(s.addTwoNumbers(l1=mk([9],mod), l2=mk([9],mod))), [8, 1])
    eq(out(s.addTwoNumbers(l1=mk([9, 9, 9],mod), l2=mk([1],mod))), [0, 0, 0, 1])
