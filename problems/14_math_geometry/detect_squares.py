"""
Detect Squares (Medium)

Design a class DetectSquares for points on a plane.

- add(point) adds a point [x, y]. Duplicate points count separately.
- count(point) returns how many ways you can choose three added points that form an axis-aligned square of positive area with the query point.

Example 1:
d = DetectSquares()
d.add([1, 1])
d.add([2, 2])
d.add([1, 2])
d.count([2, 1])  ->  1
d.count([3, 3])  ->  0
d.add([2, 2])
d.count([2, 1])  ->  2
Explanation: The duplicate [2, 2] gives a second way to form the same square.

Constraints:
- Coordinates are between 0 and 1,000
"""

class DetectSquares:
    def __init__(self):
        pass

    def add(self, point: list[int]) -> None:
        pass

    def count(self, point: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
