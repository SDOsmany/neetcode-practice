"""
Regular Expression Matching (Hard)

Return True if pattern p matches the whole of s. In p, "." matches any one character, and "*" means zero or more of the character before it.

Example 1:
Input: s = "aa", p = ".b"
Output: False

Example 2:
Input: s = "nnn", p = "n*"
Output: True
Explanation: "n*" can repeat n three times.

Example 3:
Input: s = "nb", p = ".*b"
Output: True

Constraints:
- 1 <= len(s), len(p) <= 50
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
