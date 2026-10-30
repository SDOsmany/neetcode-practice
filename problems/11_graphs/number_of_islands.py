"""
Number of Islands (Medium)

grid is a 2D map where "1" is land and "0" is water. An island is a group of land cells connected horizontally or vertically. Diagonal cells don't connect. Return the number of islands. You may modify grid.

Example 1:
Input: grid = [["1", "1", "0"], ["0", "1", "0"], ["0", "0", "1"]]
Output: 2
Explanation: The top three land cells form one island. The bottom-right cell touches them only diagonally, so it's a second island.

Example 2:
Input: grid = [["1", "1"], ["1", "1"]]
Output: 1
Explanation: All the land is connected.

Example 3:
Input: grid = [["0"]]
Output: 0
Explanation: There's no land.

Constraints:
- 1 <= rows, columns <= 100
- Each cell is "0" or "1"
"""

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
