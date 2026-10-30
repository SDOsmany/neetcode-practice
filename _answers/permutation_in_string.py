"""
Permutation In String (Medium)

You're given two strings, s1 and s2. Return True if some substring of s2 uses exactly the same letters as s1, the same number of times each, in any order. Otherwise return False.

Example 1:
Input: s1 = "abc", s2 = "lecabee"
Output: True
Explanation: s2 contains "cab", which is a rearrangement of "abc".

Example 2:
Input: s1 = "abc", s2 = "lecaabee"
Output: False
Explanation: The letters are all present, but no 3 consecutive letters use exactly a, b and c.

Example 3:
Input: s1 = "ab", s2 = "a"
Output: False
Explanation: s2 is shorter than s1, so no match is possible.

Constraints:
- 1 <= len(s1), len(s2) <= 1,000
- Both strings contain lowercase English letters only
"""

from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = Counter(s1)
        window = Counter(s2[:len(s1)])
        if window == need:
            return True
        for r in range(len(s1), len(s2)):
            window[s2[r]] += 1
            left = s2[r - len(s1)]
            window[left] -= 1
            if window[left] == 0:
                del window[left]
            if window == need:
                return True
        return False


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
