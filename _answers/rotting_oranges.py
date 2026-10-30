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

from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        q = deque()
        fresh = 0
        for r, row in enumerate(grid):
            for c, v in enumerate(row):
                if v == 2:
                    q.append((r, c))
                elif v == 1:
                    fresh += 1
        minutes = 0
        while q and fresh:
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 1:
                        grid[x][y] = 2
                        fresh -= 1
                        q.append((x, y))
        return minutes if fresh == 0 else -1


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
