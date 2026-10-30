"""
Distinct Subsequences (Hard)

Return how many different ways you can pick characters from s, keeping their order, to spell t. Two ways differ if they use different positions.

Example 1:
Input: s = "caaat", t = "cat"
Output: 3
Explanation: Each of the three "a" positions gives one way.

Example 2:
Input: s = "xxyxy", t = "xy"
Output: 5

Example 3:
Input: s = "abc", t = "d"
Output: 0

Constraints:
- 1 <= len(s), len(t) <= 1,000
"""

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
