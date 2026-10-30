"""
Insert Interval (Medium)

intervals is a sorted list of non-overlapping [start, end] pairs. Insert newInterval, merging wherever needed, and return the sorted result.

Example 1:
Input: intervals = [[1, 3], [4, 6]], newInterval = [2, 5]
Output: [[1, 6]]

Example 2:
Input: intervals = [[1, 2], [3, 5], [9, 10]], newInterval = [6, 7]
Output: [[1, 2], [3, 5], [6, 7], [9, 10]]

Example 3:
Input: intervals = [], newInterval = [1, 2]
Output: [[1, 2]]

Constraints:
- 0 <= len(intervals) <= 1,000
"""

class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
