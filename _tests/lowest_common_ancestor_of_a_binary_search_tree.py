
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
    root = mk([5,3,8,1,4,7,9,None,2], mod)
    n3, n8, n1, n4 = root.left, root.right, root.left.left, root.left.right
    eq(s.lowestCommonAncestor(root,n3,n8).val, 5)
    eq(s.lowestCommonAncestor(root,n3,n4).val, 3)
    eq(s.lowestCommonAncestor(root,n1,n4).val, 3)
    eq(s.lowestCommonAncestor(root,n8.left,n8.right).val, 8)
