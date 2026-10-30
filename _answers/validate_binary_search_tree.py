"""
Validate Binary Search Tree (Medium)

Return True if the tree is a valid binary search tree: every value in a node's left subtree is strictly smaller than it, and every value in its right subtree is strictly larger.

Example 1:
Input: root = [2, 1, 3]
Output: True

Example 2:
Input: root = [1, 2, 3]
Output: False

Example 3:
Input: root = [5, 4, 6, None, None, 3, 7]
Output: False
Explanation: 3 is in the right subtree of 5, so it must be larger than 5.

Constraints:
- 1 <= number of nodes <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: "TreeNode | None") -> bool:
        def ok(n, low, high):
            if not n:
                return True
            return low < n.val < high and ok(n.left, low, n.val) and ok(n.right, n.val, high)
        return ok(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
