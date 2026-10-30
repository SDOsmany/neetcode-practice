"""
Palindromic Substrings (Medium)

Return how many substrings of s are palindromes. Substrings at different positions count separately, even if they have the same text.

Example 1:
Input: s = "abc"
Output: 3
Explanation: Only the three single letters.

Example 2:
Input: s = "aaa"
Output: 6
Explanation: "a" three times, "aa" twice and "aaa" once.

Example 3:
Input: s = "abba"
Output: 6

Constraints:
- 1 <= len(s) <= 1,000
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
