"""
Longest Repeating Character Replacement (Medium)

s contains uppercase letters. You may change at most k characters to any other uppercase letter. Return the length of the longest substring you can make contain just one repeated letter.

Example 1:
Input: s = "XYYX", k = 2
Output: 4
Explanation: Change both X to Y, or both Y to X.

Example 2:
Input: s = "AAABABB", k = 1
Output: 5
Explanation: Change the B at index 3 to get "AAAAA".

Example 3:
Input: s = "A", k = 0
Output: 1

Constraints:
- 1 <= len(s) <= 1,000
- 0 <= k <= len(s)
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
