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
        res = []
        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while top <= bottom and left <= right:
            res += matrix[top][left:right + 1]
            top += 1
            res += [matrix[r][right] for r in range(top, bottom + 1)]
            right -= 1
            if top <= bottom:
                res += matrix[bottom][left:right + 1][::-1]
                bottom -= 1
            if left <= right:
                res += [matrix[r][left] for r in range(bottom, top - 1, -1)]
                left += 1
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
