"""
Spiral Matrix (Medium)

Return all values of matrix in clockwise spiral order, starting from the top-left.

Example 1:
Input: matrix = [[1, 2], [3, 4]]
Output: [1, 2, 4, 3]

Example 2:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

Example 3:
Input: matrix = [[1, 2, 3, 4]]
Output: [1, 2, 3, 4]

Constraints:
- 1 <= rows, columns <= 10
"""

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
