"""
Meeting Rooms (Easy)

intervals lists meeting times as [start, end]. Return True if one person could attend them all. A meeting can start exactly when another ends.

Example 1:
Input: intervals = [[0, 30], [5, 10], [15, 20]]
Output: False

Example 2:
Input: intervals = [[5, 8], [9, 15]]
Output: True

Example 3:
Input: intervals = [[1, 2], [2, 3]]
Output: True
Explanation: Meetings can touch.

Constraints:
- 0 <= len(intervals) <= 500
"""

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        times = sorted(intervals)
        return all(a[1] <= b[0] for a, b in zip(times, times[1:]))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
