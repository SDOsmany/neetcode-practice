"""
Daily Temperatures (Medium)

temperatures[i] is the temperature on day i. Return an array where result[i] is the number of days you must wait after day i for a strictly warmer day. If no warmer day comes, result[i] is 0.

Example 1:
Input: temperatures = [30, 38, 30, 36, 35, 40, 28]
Output: [1, 4, 1, 2, 1, 0, 0]
Explanation: Day 1 (38) waits 4 days for 40 on day 5. Nothing after day 5 beats 40, and nothing follows day 6.

Example 2:
Input: temperatures = [22, 21, 20]
Output: [0, 0, 0]
Explanation: It only gets colder.

Example 3:
Input: temperatures = [1, 2, 3]
Output: [1, 1, 0]
Explanation: Each day is beaten by the next, except the last.

Constraints:
- 1 <= len(temperatures) <= 1,000
- 1 <= temperatures[i] <= 100
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                res[j] = i - j
            stack.append(i)
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
