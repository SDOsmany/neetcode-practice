"""
Course Schedule (Medium)

There are numCourses courses, numbered from 0. Each pair [a, b] in prerequisites means you must take b before a. Return True if you can finish all the courses.

Example 1:
Input: numCourses = 2, prerequisites = [[0, 1]]
Output: True
Explanation: Take course 1, then course 0.

Example 2:
Input: numCourses = 2, prerequisites = [[0, 1], [1, 0]]
Output: False
Explanation: Each course requires the other.

Example 3:
Input: numCourses = 3, prerequisites = []
Output: True

Constraints:
- 1 <= numCourses <= 1,000
- All pairs are distinct
"""

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        needs = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            needs[a].append(b)
        state = [0] * numCourses
        def ok(c):
            if state[c]:
                return state[c] == 2
            state[c] = 1
            if not all(ok(p) for p in needs[c]):
                return False
            state[c] = 2
            return True
        return all(ok(c) for c in range(numCourses))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
