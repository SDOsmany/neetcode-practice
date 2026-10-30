"""
Non Overlapping Intervals (Medium)

Return the fewest intervals to remove so that the rest don't overlap. Intervals that only touch, like [1, 2] and [2, 3], don't count as overlapping.

Example 1:
Input: intervals = [[1, 2], [2, 4], [1, 4]]
Output: 1
Explanation: Remove [1, 4].

Example 2:
Input: intervals = [[1, 2], [2, 4]]
Output: 0

Example 3:
Input: intervals = [[1, 2], [1, 2], [1, 2]]
Output: 2

Constraints:
- 1 <= len(intervals) <= 1,000
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        removed = 0
        end = float("-inf")
        for s, e in sorted(intervals, key=lambda x: x[1]):
            if s >= end:
                end = e
            else:
                removed += 1
        return removed


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
