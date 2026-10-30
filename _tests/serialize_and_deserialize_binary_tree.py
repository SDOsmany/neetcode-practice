
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
    c = mod.Codec()
    for t in ([1,2,3,None,None,4,5], [], [1], [-1,-2,None,-3], [1,None,2,None,3]):
        eq(out(c.deserialize(c.serialize(mk(t, mod)))), t)
