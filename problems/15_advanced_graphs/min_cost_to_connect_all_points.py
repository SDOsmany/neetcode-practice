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

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
