"""
Longest Increasing Path In a Matrix (Hard)

From any cell you may move up, down, left or right to a strictly larger value. Return the number of cells in the longest such path.

Example 1:
Input: matrix = [[5, 5, 3], [2, 3, 6], [1, 1, 1]]
Output: 4
Explanation: 1 -> 2 -> 3 -> 6.

Example 2:
Input: matrix = [[1, 2, 3], [2, 1, 4], [7, 6, 5]]
Output: 7
Explanation: 1, 2, 3, 4, 5, 6, 7.

Example 3:
Input: matrix = [[1]]
Output: 1

Constraints:
- 1 <= rows, columns <= 100
"""

from functools import lru_cache

class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        @lru_cache(None)
        def go(r, c):
            best = 1
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[r][c]:
                    best = max(best, 1 + go(x, y))
            return best
        return max(go(r, c) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
