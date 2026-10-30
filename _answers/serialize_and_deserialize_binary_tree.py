"""
Serialize And Deserialize Binary Tree (Hard)

Design a class Codec. serialize(root) turns a binary tree into a string, and deserialize(data) rebuilds the same tree from that string. You can choose any string format.

Example 1:
c = Codec()
c.deserialize(c.serialize(root)), with root = [1, 2, 3, None, None, 4, 5]  ->  [1, 2, 3, None, None, 4, 5]
Explanation: The rebuilt tree must match the original.

Example 2:
c.deserialize(c.serialize(None))  ->  None
Explanation: An empty tree has to survive too.

Constraints:
- 0 <= number of nodes <= 1,000
- Values can be negative
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: "TreeNode | None") -> str:
        out = []
        def dfs(n):
            if not n:
                out.append("N")
                return
            out.append(str(n.val))
            dfs(n.left)
            dfs(n.right)
        dfs(root)
        return ",".join(out)

    def deserialize(self, data: str) -> "TreeNode | None":
        vals = iter(data.split(","))
        def build():
            v = next(vals)
            if v == "N":
                return None
            n = TreeNode(int(v))
            n.left = build()
            n.right = build()
            return n
        return build()


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
