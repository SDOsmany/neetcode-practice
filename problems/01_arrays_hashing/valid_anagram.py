"""
Valid Anagram (Easy)

Return True if t uses exactly the same letters as s, the same number of times each, in any order. Otherwise return False.

Example 1:
Input: s = "racecar", t = "carrace"
Output: True
Explanation: Both use the same letters the same number of times.

Example 2:
Input: s = "jar", t = "jam"
Output: False
Explanation: "r" and "m" differ.

Example 3:
Input: s = "ab", t = "abb"
Output: False
Explanation: The lengths differ.

Constraints:
- 1 <= len(s), len(t) <= 50,000
- Lowercase English letters only
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
