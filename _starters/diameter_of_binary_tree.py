"""
Diameter of Binary Tree (Easy)

The diameter of a binary tree is the number of edges on the longest path between any two nodes. The path doesn't have to pass through the root. Return the diameter.

Example 1:
Input: root = [1, None, 2, 3, 4, 5]
Output: 3
Explanation: The longest path is 5 -> 3 -> 2 -> 4, which has three edges.

Example 2:
Input: root = [1, 2, 3]
Output: 2

Example 3:
Input: root = [1]
Output: 0

Constraints:
- 1 <= number of nodes <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: "TreeNode | None") -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
