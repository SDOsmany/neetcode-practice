"""
Lowest Common Ancestor of a Binary Search Tree (Medium)

root is a binary search tree, and p and q are two different nodes in it. Return the lowest node that has both p and q as descendants. A node counts as a descendant of itself.

Example 1:
root = [5, 3, 8, 1, 4, 7, 9, None, 2], p is node 3, q is node 8  ->  node 5
Explanation: They're on opposite sides of 5.

Example 2:
Same tree, p is node 3, q is node 4  ->  node 3
Explanation: A node is its own descendant, so 3 is the answer.

Constraints:
- 2 <= number of nodes <= 100
- All values are distinct
- p and q are both in the tree
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        node = root
        while True:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                return node


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
