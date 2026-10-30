"""
Evaluate Reverse Polish Notation (Medium)

tokens is an arithmetic expression in Reverse Polish Notation, where each operator comes after its two operands. Operators are "+", "-", "*" and "/". Division truncates toward zero. Return the result.

Example 1:
Input: tokens = ["1", "2", "+", "3", "*", "4", "-"]
Output: 5
Explanation: ((1 + 2) * 3) - 4 = 5.

Example 2:
Input: tokens = ["6", "-4", "/"]
Output: -1
Explanation: -1.5 truncates toward zero, to -1.

Example 3:
Input: tokens = ["7"]
Output: 7

Constraints:
- 1 <= len(tokens) <= 1,000
- The expression is always valid
- There is no division by zero
"""

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
