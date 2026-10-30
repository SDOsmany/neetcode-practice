"""
Longest Palindromic Substring (Medium)

Return the longest substring of s that reads the same forwards and backwards. If several are tied for longest, any of them is accepted.

Example 1:
Input: s = "ababd"
Output: "aba"
Explanation: "bab" is equally long and also accepted.

Example 2:
Input: s = "abbc"
Output: "bb"
Explanation: Palindromes can have an even length.

Example 3:
Input: s = "x"
Output: "x"
Explanation: One character is always a palindrome.

Constraints:
- 1 <= len(s) <= 1,000
- s contains English letters and digits
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for i in range(len(s)):
            for l, r in ((i, i), (i, i + 1)):
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l -= 1
                    r += 1
                if r - l - 1 > len(best):
                    best = s[l + 1:r]
        return best


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
