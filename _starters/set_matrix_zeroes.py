"""
Set Matrix Zeroes (Medium)

If a cell is 0, set its whole row and column to 0. Change matrix in place and return nothing. As a follow-up, use only O(1) extra space.

Example 1:
Input: matrix = [[0, 1], [1, 1]]
Output: [[0, 0], [0, 1]]

Example 2:
Input: matrix = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
Output: [[1, 0, 3], [0, 0, 0], [6, 0, 8]]

Example 3:
Input: matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
Output: [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]

Constraints:
- 1 <= rows, columns <= 100
"""

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
