"""
Number of 1 Bits (Easy)

Return how many bits are set to 1 in the binary form of the non-negative integer n.

Example 1:
Input: n = 23
Output: 4
Explanation: 23 is 10111 in binary.

Example 2:
Input: n = 2147483645
Output: 30

Example 3:
Input: n = 0
Output: 0

Constraints:
- 0 <= n < 2^32
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
