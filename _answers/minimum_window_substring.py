"""
Minimum Window Substring (Hard)

Return the shortest substring of s that contains every character of t, including repeats. If there is no such substring, return "". Each input has at most one shortest answer.

Example 1:
Input: s = "OUZODYXAZV", t = "XYZ"
Output: "YXAZ"
Explanation: It's the shortest piece containing X, Y and Z.

Example 2:
Input: s = "xyz", t = "xyz"
Output: "xyz"

Example 3:
Input: s = "x", t = "xy"
Output: ""
Explanation: s has no y.

Constraints:
- 1 <= len(s), len(t) <= 1,000
- English letters only
"""

from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        best = ""
        l = 0
        for r, c in enumerate(s):
            if need[c] > 0:
                missing -= 1
            need[c] -= 1
            while missing == 0:
                if not best or r - l + 1 < len(best):
                    best = s[l:r + 1]
                need[s[l]] += 1
                if need[s[l]] > 0:
                    missing += 1
                l += 1
        return best


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
