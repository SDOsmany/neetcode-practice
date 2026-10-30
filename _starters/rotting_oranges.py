"""
Rotting Oranges (Medium)

grid is a 2D map where 0 is an empty cell, 1 is a fresh orange and 2 is a rotten orange. Every minute, each fresh orange directly above, below, left or right of a rotten one becomes rotten. Return the minutes needed until no fresh orange remains. If some fresh orange can never rot, return -1.

Example 1:
Input: grid = [[1, 1, 0], [0, 1, 1], [0, 1, 2]]
Output: 4
Explanation: Rot spreads from the bottom-right corner, and the top-left orange is reached in minute 4.

Example 2:
Input: grid = [[1, 0, 1], [0, 2, 0], [1, 0, 1]]
Output: -1
Explanation: The fresh oranges touch the rotten one only diagonally.

Example 3:
Input: grid = [[0]]
Output: 0
Explanation: With no fresh oranges, no time is needed.

Constraints:
- 1 <= rows, columns <= 10
- Each cell is 0, 1 or 2
"""

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
