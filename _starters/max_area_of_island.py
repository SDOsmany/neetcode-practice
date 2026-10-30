"""
Max Area of Island (Medium)

grid holds 1 for land and 0 for water. Land connects horizontally and vertically. Return the size of the largest island, or 0 if there's no land.

Example 1:
Input: grid = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1], [0, 1, 1, 0, 1], [0, 1, 0, 0, 1]]
Output: 6
Explanation: The island in the middle has six cells.

Example 2:
Input: grid = [[0, 0]]
Output: 0

Example 3:
Input: grid = [[1]]
Output: 1

Constraints:
- 1 <= rows, columns <= 50
"""

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
