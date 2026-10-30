"""
Meeting Rooms II (Medium)

intervals lists meeting times as [start, end]. Return the fewest rooms needed to hold them all. A room is free for a new meeting at the moment another ends.

Example 1:
Input: intervals = [[0, 40], [5, 10], [15, 20]]
Output: 2

Example 2:
Input: intervals = [[4, 9]]
Output: 1

Example 3:
Input: intervals = [[1, 2], [2, 3]]
Output: 1

Constraints:
- 0 <= len(intervals) <= 500
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        ends = []
        for s, e in sorted(intervals):
            if ends and ends[0] <= s:
                heapq.heapreplace(ends, e)
            else:
                heapq.heappush(ends, e)
        return len(ends)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
