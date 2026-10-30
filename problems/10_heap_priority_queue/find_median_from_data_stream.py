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

class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
