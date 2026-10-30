"""
Binary Tree Maximum Path Sum (Hard)

A path is a sequence of connected nodes that uses each node at most once. It doesn't have to include the root. Return the largest sum of values along any non-empty path.

Example 1:
Input: root = [1, 2, 3]
Output: 6
Explanation: The path 2 -> 1 -> 3 adds up to 6.

Example 2:
Input: root = [-15, 10, 20, None, None, 15, 5, -5]
Output: 40
Explanation: The path 15 -> 20 -> 5 adds up to 40.

Example 3:
Input: root = [-3]
Output: -3
Explanation: A path must contain at least one node.

Constraints:
- 1 <= number of nodes <= 1,000
- -1,000 <= Node.val <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: "TreeNode") -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
