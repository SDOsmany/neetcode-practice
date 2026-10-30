"""
Kth Smallest Element In a BST (Medium)

Given a binary search tree, return the kth smallest value, counting from 1.

Example 1:
Input: root = [2, 1, 3], k = 1
Output: 1

Example 2:
Input: root = [4, 3, 5, 2, None], k = 4
Output: 5
Explanation: In sorted order the values are 2, 3, 4, 5.

Example 3:
Input: root = [5, 3, 6, 2, 4, None, None, 1], k = 3
Output: 3

Constraints:
- 1 <= k <= number of nodes <= 1,000
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: "TreeNode", k: int) -> int:
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.val
            node = node.right


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
