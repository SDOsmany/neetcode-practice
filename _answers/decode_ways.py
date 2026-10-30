"""
Decode Ways (Medium)

Letters are encoded as numbers, with A as "1" through Z as "26". Given a string of digits, return how many ways it can be decoded. A piece can't start with "0".

Example 1:
Input: s = "12"
Output: 2
Explanation: "AB" or "L".

Example 2:
Input: s = "226"
Output: 3
Explanation: 2 2 6, 22 6, or 2 26.

Example 3:
Input: s = "01"
Output: 0
Explanation: A piece can't start with 0.

Constraints:
- 1 <= len(s) <= 100
- Digits only
"""

class Solution:
    def numDecodings(self, s: str) -> int:
        prev, cur = 0, 1
        for i, d in enumerate(s):
            nxt = cur if d != "0" else 0
            if i and "10" <= s[i - 1:i + 1] <= "26":
                nxt += prev
            prev, cur = cur, nxt
        return cur


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
