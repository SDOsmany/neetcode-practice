"""
K Closest Points to Origin (Medium)

points[i] = [x, y] is a point on a plane. Return the k points closest to the origin (0, 0), by straight-line distance. The output can be in any order. Inputs won't have a tie at the cut-off that changes the answer.

Example 1:
Input: points = [[0, 2], [2, 2]], k = 1
Output: [[0, 2]]
Explanation: [0, 2] is distance 2 away and [2, 2] is about 2.83 away.

Example 2:
Input: points = [[0, 2], [2, 0], [2, 2]], k = 2
Output: [[0, 2], [2, 0]]
Explanation: The two points at distance 2 are closest.

Example 3:
Input: points = [[3, 3], [5, -1], [-2, 4]], k = 2
Output: [[3, 3], [-2, 4]]
Explanation: Squared distances are 18, 26 and 20, so the middle point is left out.

Constraints:
- 1 <= k <= len(points) <= 1,000
- -100 <= x, y <= 100
"""

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
