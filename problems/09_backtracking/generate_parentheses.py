"""
Generate Parentheses (Medium)

Return every string made of n opening and n closing parentheses that is well formed, meaning each "(" has a matching ")" after it. Any output order is fine.

Example 1:
Input: n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
Explanation: There are exactly five ways to arrange three pairs.

Example 2:
Input: n = 1
Output: ["()"]
Explanation: There's only one arrangement.

Constraints:
- 1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
