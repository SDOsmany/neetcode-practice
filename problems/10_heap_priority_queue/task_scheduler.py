"""
Task Scheduler (Medium)

tasks lists single-letter tasks, each taking one time unit. Two tasks with the same letter must have at least n units between them. The CPU may stay idle. Return the fewest time units needed to finish all the tasks.

Example 1:
Input: tasks = ["X", "X", "Y", "Y"], n = 2
Output: 5
Explanation: X, Y, idle, X, Y.

Example 2:
Input: tasks = ["A", "A", "A", "B", "C"], n = 3
Output: 9
Explanation: A, B, C, idle, A, idle, idle, idle, A.

Example 3:
Input: tasks = ["A", "B", "C"], n = 5
Output: 3

Constraints:
- 1 <= len(tasks) <= 1,000
- 0 <= n <= 100
"""

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
