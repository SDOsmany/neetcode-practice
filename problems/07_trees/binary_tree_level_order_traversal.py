"""
Binary Tree Level Order Traversal (Medium)

You're given the root of a binary tree. Return its values level by level, as a list of lists. Each inner list holds one level's values, from left to right, starting with the root.

Example 1:
Input: root = [1, 2, 3, 4, 5, 6, 7]
Output: [[1], [2, 3], [4, 5, 6, 7]]
Explanation: The tree has three full levels.

Example 2:
Input: root = [1]
Output: [[1]]
Explanation: A single node is one level.

Example 3:
Input: root = []
Output: []
Explanation: An empty tree has no levels.

Constraints:
- 0 <= number of nodes <= 1,000
- -1,000 <= Node.val <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: "TreeNode | None") -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
