"""
Longest Common Subsequence (Medium)

Return the length of the longest sequence of characters that appears in both strings in the same order, not necessarily next to each other.

Example 1:
Input: text1 = "cat", text2 = "crabt"
Output: 3
Explanation: "cat" is in "crabt" in order.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0

Constraints:
- 1 <= len(text1), len(text2) <= 1,000
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
