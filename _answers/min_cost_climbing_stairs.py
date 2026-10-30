"""
Min Cost Climbing Stairs (Easy)

cost[i] is the price of stepping on stair i. After paying, you climb 1 or 2 stairs. You can start at stair 0 or 1. Return the lowest total cost to get past the last stair.

Example 1:
Input: cost = [1, 2, 3]
Output: 2
Explanation: Start at stair 1, pay 2 and climb two stairs to the top.

Example 2:
Input: cost = [1, 2, 1, 2, 1, 1, 1]
Output: 4

Example 3:
Input: cost = [5, 5]
Output: 5

Constraints:
- 2 <= len(cost) <= 100
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        a, b = 0, 0
        for c in cost:
            a, b = b, min(a, b) + c
        return min(a, b)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
