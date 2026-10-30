"""
Maximum Depth of Binary Tree (Easy)

You're given the root of a binary tree. Return its depth: the number of nodes on the longest path from the root down to a leaf. A leaf is a node with no children.

Example 1:
Input: root = [1, 2, 3, None, None, 4]
Output: 3
Explanation: The longest path is 1 -> 3 -> 4, which has three nodes.

Example 2:
Input: root = []
Output: 0
Explanation: An empty tree has depth 0.

Example 3:
Input: root = [1]
Output: 1
Explanation: The root alone counts as one node.

Constraints:
- 0 <= number of nodes <= 100
- -100 <= Node.val <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: "TreeNode | None") -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
