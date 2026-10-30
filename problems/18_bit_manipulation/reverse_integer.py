"""
Reverse Integer (Medium)

Reverse the digits of the 32-bit signed integer x, keeping its sign. If the result falls outside the range -2^31 to 2^31 - 1, return 0.

Example 1:
Input: x = 1234
Output: 4321

Example 2:
Input: x = -1234
Output: -4321

Example 3:
Input: x = 120
Output: 21
Explanation: Leading zeros disappear.

Constraints:
- -2^31 <= x <= 2^31 - 1
"""

class Solution:
    def reverse(self, x: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
