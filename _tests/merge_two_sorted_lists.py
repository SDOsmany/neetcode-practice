
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
    eq(out(s.mergeTwoLists(mk([1,2,4],mod),mk([1,3,5],mod))), [1,1,2,3,4,5])
    eq(out(s.mergeTwoLists(mk([],mod),mk([1,2],mod))), [1,2])
    eq(out(s.mergeTwoLists(mk([],mod),mk([],mod))), [])
