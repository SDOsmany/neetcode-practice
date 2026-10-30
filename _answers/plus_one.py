"""
Plus One (Easy)

digits holds a non-negative integer, most significant digit first. Add 1 and return the digits of the result.

Example 1:
Input: digits = [1, 2, 3, 4]
Output: [1, 2, 3, 5]

Example 2:
Input: digits = [9, 9, 9]
Output: [1, 0, 0, 0]

Example 3:
Input: digits = [0]
Output: [1]

Constraints:
- 1 <= len(digits) <= 100
"""

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        res = digits[:]
        for i in range(len(res) - 1, -1, -1):
            if res[i] < 9:
                res[i] += 1
                return res
            res[i] = 0
        return [1] + res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
