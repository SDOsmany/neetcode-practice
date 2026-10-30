"""
Climbing Stairs (Easy)

You're at the bottom of a staircase with n steps. Each move climbs either 1 or 2 steps. Return the number of different sequences of moves that get you to the top.

Example 1:
Input: n = 2
Output: 2
Explanation: 1 + 1, or 2.

Example 2:
Input: n = 3
Output: 3
Explanation: 1 + 1 + 1, 1 + 2, or 2 + 1.

Example 3:
Input: n = 10
Output: 89
Explanation: Larger inputs need more than plain recursion, because the tests go up to n = 40.

Constraints:
- 1 <= n <= 45
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        for _ in range(n):
            a, b = b, a + b
        return a


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
