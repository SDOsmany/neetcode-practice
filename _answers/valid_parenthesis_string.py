"""
Valid Parenthesis String (Medium)

s contains "(", ")" and "*". A "*" can act as "(", ")" or nothing. Return True if some choice makes s balanced.

Example 1:
Input: s = "((**)"
Output: True
Explanation: One * acts as ) and the other as nothing.

Example 2:
Input: s = "(((*)"
Output: False

Example 3:
Input: s = "*)"
Output: True

Constraints:
- 1 <= len(s) <= 100
"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0
        for c in s:
            low += 1 if c == "(" else -1
            high += -1 if c == ")" else 1
            if high < 0:
                return False
            low = max(low, 0)
        return low == 0


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
