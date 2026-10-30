"""
Count Good Nodes In Binary Tree (Medium)

A node is good if no node on the path from the root to it has a larger value. Return how many good nodes the tree has.

Example 1:
Input: root = [2, 1, 1, 3, None, 1, 5]
Output: 3
Explanation: The good nodes are the root 2, the 3 and the 5.

Example 2:
Input: root = [1, 2, -1, 3, 4]
Output: 4

Example 3:
Input: root = [1]
Output: 1

Constraints:
- 1 <= number of nodes <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: "TreeNode") -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
