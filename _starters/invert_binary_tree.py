"""
Invert Binary Tree (Easy)

You're given the root of a binary tree. Mirror it by swapping the left and right children of every node, and return the root. In the examples, a tree is written level by level, with None marking a missing child.

Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 2, 7, 6, 5, 4]
Explanation: Every level comes out in reverse order.

Example 2:
Input: root = [3, 2, 1]
Output: [3, 1, 2]
Explanation: The two children swap.

Example 3:
Input: root = []
Output: []
Explanation: An empty tree stays empty.

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
    def invertTree(self, root: "TreeNode | None") -> "TreeNode | None":
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
