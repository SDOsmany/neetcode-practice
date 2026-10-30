"""
Interleaving String (Medium)

Return True if s3 can be formed by weaving s1 and s2 together, keeping the characters of each in their own order and using all of them.

Example 1:
Input: s1 = "aaaa", s2 = "bbbb", s3 = "aabbbbaa"
Output: True

Example 2:
Input: s1 = "abc", s2 = "xyz", s3 = "abxzcy"
Output: False
Explanation: "z" comes before "y", which breaks the order of s2.

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: True

Constraints:
- 0 <= len(s1), len(s2) <= 100
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        ok = [False] * (len(s2) + 1)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                if i == 0 and j == 0:
                    ok[j] = True
                else:
                    ok[j] = (i > 0 and ok[j] and s1[i - 1] == s3[i + j - 1]) or (j > 0 and ok[j - 1] and s2[j - 1] == s3[i + j - 1])
        return ok[-1]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
