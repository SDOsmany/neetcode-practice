
def mk(vals, mod):
    if not vals:
        return None
    nodes = [None if v is None else mod.TreeNode(v) for v in vals]
    kids = nodes[1:][::-1]
    for n in nodes:
        if n:
            if kids: n.left = kids.pop()
            if kids: n.right = kids.pop()
    return nodes[0]
def out(root):
    r, q = [], [root]
    while q:
        n = q.pop(0)
        if n:
            r.append(n.val); q += [n.left, n.right]
        else:
            r.append(None)
    while r and r[-1] is None:
        r.pop()
    return r

def check(mod, eq):
    s = mod.Solution()
    eq(s.isBalanced(root=mk([1, 2, 3, None, None, 4],mod)), True)
    eq(s.isBalanced(root=mk([1, 2, 3, None, None, 4, None, 5],mod)), False)
    eq(s.isBalanced(root=mk([],mod)), True)
