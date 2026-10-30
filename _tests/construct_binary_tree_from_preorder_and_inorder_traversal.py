
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
    eq(out(s.buildTree(preorder=[1, 2, 3, 4], inorder=[2, 1, 3, 4])), [1, 2, 3, None, None, None, 4])
    eq(out(s.buildTree(preorder=[1], inorder=[1])), [1])
    eq(out(s.buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])), [3, 9, 20, None, None, 15, 7])
