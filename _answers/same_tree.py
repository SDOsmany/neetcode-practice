"""
Same Tree (Easy)

Return True if the binary trees p and q have the same shape and the same value in every matching position.

Example 1:
Input: p = [1, 2, 3], q = [1, 2, 3]
Output: True

Example 2:
Input: p = [4, 7], q = [4, None, 7]
Output: False
Explanation: The same values sit on different sides.

Example 3:
Input: p = [1, 2, 3], q = [1, 3, 2]
Output: False

Constraints:
- 0 <= number of nodes <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: "TreeNode | None", q: "TreeNode | None") -> bool:
        if not p or not q:
            return p is q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
