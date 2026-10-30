"""
Search a 2D Matrix (Medium)

In matrix, each row is sorted ascending, and each row starts with a value greater than the last value of the row above. Return True if target is in the matrix. Your solution must run in O(log(rows * columns)) time.

Example 1:
Input: matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 10
Output: True
Explanation: 10 starts the second row.

Example 2:
Input: matrix = [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], target = 15
Output: False

Example 3:
Input: matrix = [[5]], target = 5
Output: True

Constraints:
- 1 <= rows, columns <= 100
"""

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
