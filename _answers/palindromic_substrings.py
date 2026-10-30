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
        count = 0
        for center in range(2 * len(s) - 1):
            l, r = center // 2, (center + 1) // 2
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
