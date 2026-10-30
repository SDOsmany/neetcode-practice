"""
Min Cost to Connect All Points (Medium)

points[i] = [x, y]. Connecting two points costs their Manhattan distance, |x1 - x2| + |y1 - y2|. Return the lowest total cost that connects all the points, directly or indirectly.

Example 1:
Input: points = [[0, 0], [2, 2], [3, 3], [2, 4], [4, 2]]
Output: 10

Example 2:
Input: points = [[3, 12], [-2, 5], [-4, 1]]
Output: 18

Example 3:
Input: points = [[0, 0]]
Output: 0
Explanation: One point needs no connections.

Constraints:
- 1 <= len(points) <= 1,000
- All points are distinct
"""

import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        seen = set()
        heap = [(0, 0)]
        total = 0
        while len(seen) < len(points):
            cost, i = heapq.heappop(heap)
            if i in seen:
                continue
            seen.add(i)
            total += cost
            for j in range(len(points)):
                if j not in seen:
                    d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heapq.heappush(heap, (d, j))
        return total


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
