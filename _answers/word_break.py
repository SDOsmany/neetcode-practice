"""
Word Break (Medium)

Return True if s can be split into a sequence of words from wordDict. A word can be used more than once.

Example 1:
Input: s = "neetcode", wordDict = ["neet", "code"]
Output: True

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: True
Explanation: "apple" is used twice.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: False

Constraints:
- 1 <= len(s) <= 200
- 1 <= len(wordDict) <= 100
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        ok = [True] + [False] * len(s)
        for i in range(1, len(s) + 1):
            ok[i] = any(ok[i - len(w)] and s.startswith(w, i - len(w)) for w in wordDict if len(w) <= i)
        return ok[-1]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
