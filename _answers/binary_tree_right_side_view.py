"""
Binary Tree Right Side View (Medium)

Imagine standing to the right of a binary tree. Return the values you can see from top to bottom: the rightmost node of each level.

Example 1:
Input: root = [1, 2, 3]
Output: [1, 3]

Example 2:
Input: root = [1, 2, 3, 4, 5, 6, 7]
Output: [1, 3, 7]

Example 3:
Input: root = [1, 2, 3, 4]
Output: [1, 3, 4]
Explanation: The rightmost node on the last level can come from the left side.

Constraints:
- 0 <= number of nodes <= 100
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: "TreeNode | None") -> list[int]:
        res = []
        level = [root] if root else []
        while level:
            res.append(level[-1].val)
            level = [c for n in level for c in (n.left, n.right) if c]
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
