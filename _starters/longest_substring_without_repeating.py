"""
Longest Substring Without Repeating Characters (Medium)

Return the length of the longest substring of s in which no character appears more than once. A substring is a run of consecutive characters.

Example 1:
Input: s = "zxyzxyz"
Output: 3
Explanation: "zxy" is one of the longest runs without a repeat.

Example 2:
Input: s = "xxxx"
Output: 1
Explanation: Any longer run would repeat "x".

Example 3:
Input: s = "abba"
Output: 2
Explanation: Both "ab" and "ba" have length 2. Watch out: when the second "a" arrives, the window must not move backwards.

Constraints:
- 0 <= len(s) <= 1,000
- s may contain any printable ASCII characters
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
