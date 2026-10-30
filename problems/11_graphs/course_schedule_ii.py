"""
Course Schedule II (Medium)

There are numCourses courses, numbered from 0. Each pair [a, b] means you must take b before a. Return any order that finishes all the courses, or an empty list if it's impossible.

Example 1:
numCourses = 3, prerequisites = [[1, 0]]  ->  [0, 1, 2]
Explanation: Any order with 0 before 1 is accepted, such as [2, 0, 1].

Example 2:
numCourses = 2, prerequisites = [[0, 1], [1, 0]]  ->  []
Explanation: There's a cycle.

Constraints:
- 1 <= numCourses <= 1,000
- All pairs are distinct
"""

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
