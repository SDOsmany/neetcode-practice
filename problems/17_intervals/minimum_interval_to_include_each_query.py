"""
Minimum Interval to Include Each Query (Hard)

intervals holds inclusive [left, right] ranges, each with size right - left + 1. For each value in queries, return the size of the smallest interval containing it, or -1 if none does. Return the answers in the original query order.

Example 1:
Input: intervals = [[1, 3], [2, 3], [3, 7], [6, 6]], queries = [2, 3, 1, 7, 6, 8]
Output: [2, 2, 3, 5, 1, -1]
Explanation: For 6, [6, 6] is the smallest range containing it.

Example 2:
Input: intervals = [[1, 4]], queries = [5]
Output: [-1]

Example 3:
Input: intervals = [[1, 4], [2, 4]], queries = [3, 3]
Output: [3, 3]

Constraints:
- 1 <= len(intervals), len(queries) <= 1,000
"""

class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
