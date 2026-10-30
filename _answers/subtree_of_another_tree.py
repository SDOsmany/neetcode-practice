"""
Subtree of Another Tree (Easy)

Return True if some node in root has a subtree identical to subRoot, in both shape and values. That subtree must include all of that node's descendants.

Example 1:
Input: root = [1, 2, 3, 4, 5], subRoot = [2, 4, 5]
Output: True

Example 2:
Input: root = [1, 2, 3, 4, 5, None, None, 6], subRoot = [2, 4, 5]
Output: False
Explanation: Node 2 also has a 6 below it, so its subtree isn't identical.

Example 3:
Input: root = [1], subRoot = [1]
Output: True

Constraints:
- 1 <= number of nodes in each tree <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: "TreeNode | None", subRoot: "TreeNode | None") -> bool:
        def same(a, b):
            if not a or not b:
                return a is b
            return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)
        if not root:
            return False
        return same(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
