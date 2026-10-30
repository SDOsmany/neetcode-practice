"""
Merge Intervals (Medium)

Merge every overlapping [start, end] pair and return the result sorted by start. Pairs that only touch, like [1, 2] and [2, 3], count as overlapping.

Example 1:
Input: intervals = [[1, 3], [1, 5], [6, 7]]
Output: [[1, 5], [6, 7]]

Example 2:
Input: intervals = [[1, 2], [2, 3]]
Output: [[1, 3]]
Explanation: Touching intervals merge.

Example 3:
Input: intervals = [[4, 5], [1, 2]]
Output: [[1, 2], [4, 5]]
Explanation: The input may not be sorted.

Constraints:
- 1 <= len(intervals) <= 1,000
"""

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
