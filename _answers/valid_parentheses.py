"""
Valid Parentheses (Easy)

s contains only the characters ( ) [ ] { }. Return True if s is balanced: every opening bracket is closed by the same type of bracket, closings happen in the right order, and nothing is left unmatched.

Example 1:
Input: s = "[]"
Output: True
Explanation: One matching pair.

Example 2:
Input: s = "([{}])"
Output: True
Explanation: Each inner pair closes before its outer pair.

Example 3:
Input: s = "[(])"
Output: False
Explanation: The "]" arrives while "(" is still the most recent open bracket.

Example 4:
Input: s = "("
Output: False
Explanation: The opening bracket is never closed.

Constraints:
- 1 <= len(s) <= 1,000
- s contains only the six bracket characters
"""

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        return not stack


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
