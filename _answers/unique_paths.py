"""
Unique Paths (Medium)

A robot starts at the top-left of an m x n grid and moves only right or down. Return how many different paths reach the bottom-right.

Example 1:
Input: m = 3, n = 6
Output: 21

Example 2:
Input: m = 3, n = 3
Output: 6

Example 3:
Input: m = 1, n = 5
Output: 1
Explanation: Only one straight line works.

Constraints:
- 1 <= m, n <= 100
"""

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for _ in range(m - 1):
            for c in range(1, n):
                row[c] += row[c - 1]
        return row[-1]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
