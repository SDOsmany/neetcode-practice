
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
    eq(out(s.reverseList(mk([0,1,2,3],mod))), [3,2,1,0])
    eq(out(s.reverseList(mk([1],mod))), [1])
    eq(out(s.reverseList(mk([],mod))), [])
