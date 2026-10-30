"""
Balanced Binary Tree (Easy)

A binary tree is balanced if, at every node, the heights of the left and right subtrees differ by at most 1. Return True if the tree is balanced.

Example 1:
Input: root = [1, 2, 3, None, None, 4]
Output: True

Example 2:
Input: root = [1, 2, 3, None, None, 4, None, 5]
Output: False
Explanation: At node 3, the left subtree has height 2 and the right subtree is empty.

Example 3:
Input: root = []
Output: True

Constraints:
- 0 <= number of nodes <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: "TreeNode | None") -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
