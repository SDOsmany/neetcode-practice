"""
Reverse Bits (Easy)

n is a 32-bit unsigned integer. Reverse the order of its 32 bits and return the resulting number.

Example 1:
Input: n = 43261596
Output: 964176192

Example 2:
Input: n = 1
Output: 2147483648
Explanation: The lowest bit moves to the highest position.

Example 3:
Input: n = 4294967295
Output: 4294967295
Explanation: All 32 bits are 1.

Constraints:
- 0 <= n < 2^32
"""

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
