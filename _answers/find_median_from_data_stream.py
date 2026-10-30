"""
Find Median From Data Stream (Hard)

Design a class MedianFinder.

- addNum(num) adds a number.
- findMedian() returns the median of all numbers so far. With an even count, that's the average of the two middle values.

Example 1:
m = MedianFinder()
m.addNum(1)
m.findMedian()  ->  1.0
m.addNum(3)
m.findMedian()  ->  2.0
m.addNum(2)
m.findMedian()  ->  2.0
Explanation: The values don't arrive in sorted order.

Constraints:
- findMedian is only called after at least one addNum
"""

import heapq

class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.high, -heapq.heappushpop(self.low, -num))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
