"""
Swim In Rising Water (Hard)

grid is an n x n map of distinct heights. At time t the water level is t, and you can move to an adjacent cell if both cells are at most t. Moving takes no time. Starting at the top-left, return the earliest time you can reach the bottom-right.

Example 1:
Input: grid = [[0, 1], [2, 3]]
Output: 3
Explanation: The bottom-right cell itself has height 3.

Example 2:
Input: grid = [[0, 1, 2, 10], [9, 14, 4, 13], [12, 3, 8, 15], [11, 5, 7, 6]]
Output: 8

Example 3:
Input: grid = [[0]]
Output: 0

Constraints:
- 1 <= n <= 50
"""

import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        heap = [(grid[0][0], 0, 0)]
        seen = {(0, 0)}
        while True:
            t, r, c = heapq.heappop(heap)
            if r == c == n - 1:
                return t
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if 0 <= x < n and 0 <= y < n and (x, y) not in seen:
                    seen.add((x, y))
                    heapq.heappush(heap, (max(t, grid[x][y]), x, y))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
