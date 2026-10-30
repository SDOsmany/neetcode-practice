"""
Counting Bits (Easy)

Return a list of length n + 1 where result[i] is the number of 1 bits in i.

Example 1:
Input: n = 4
Output: [0, 1, 1, 2, 1]

Example 2:
Input: n = 0
Output: [0]

Example 3:
Input: n = 7
Output: [0, 1, 1, 2, 1, 2, 2, 3]

Constraints:
- 0 <= n <= 1,000
"""

class Solution:
    def countBits(self, n: int) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
