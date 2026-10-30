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
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
