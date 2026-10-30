"""
Rotate Image (Medium)

matrix is n x n. Rotate it 90 degrees clockwise, in place, and return nothing.

Example 1:
Input: matrix = [[1, 2], [3, 4]]
Output: [[3, 1], [4, 2]]

Example 2:
Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Constraints:
- 1 <= n <= 20
"""

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
