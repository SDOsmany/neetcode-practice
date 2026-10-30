"""
Sum of Two Integers (Medium)

Return a + b without using + or -. Treat values as 32-bit signed integers. In Python, you'll need a mask, because its integers have unlimited size.

Example 1:
Input: a = 1, b = 1
Output: 2

Example 2:
Input: a = 4, b = 7
Output: 11

Example 3:
Input: a = -2, b = 3
Output: 1
Explanation: This one is where Python needs the mask.

Constraints:
- -1,000 <= a, b <= 1,000
"""

class Solution:
    def getSum(self, a: int, b: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
