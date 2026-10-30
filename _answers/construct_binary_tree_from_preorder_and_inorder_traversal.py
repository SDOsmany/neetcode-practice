"""
Construct Binary Tree From Preorder And Inorder Traversal (Medium)

preorder and inorder are two traversals of the same binary tree, and all values are distinct. Build the tree and return its root.

Example 1:
Input: preorder = [1, 2, 3, 4], inorder = [2, 1, 3, 4]
Output: [1, 2, 3, None, None, None, 4]
Explanation: 1 is the root, 2 is on its left, and 3 and 4 are on its right.

Example 2:
Input: preorder = [1], inorder = [1]
Output: [1]

Example 3:
Input: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]
Output: [3, 9, 20, None, None, 15, 7]

Constraints:
- 1 <= len(preorder) == len(inorder) <= 1,000
- All values are distinct
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> "TreeNode | None":
        where = {v: i for i, v in enumerate(inorder)}
        next_root = iter(preorder)
        def build(lo, hi):
            if lo > hi:
                return None
            node = TreeNode(next(next_root))
            node.left = build(lo, where[node.val] - 1)
            node.right = build(where[node.val] + 1, hi)
            return node
        return build(0, len(inorder) - 1)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
