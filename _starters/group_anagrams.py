"""
Group Anagrams (Medium)

You're given a list of lowercase strings. Two strings are anagrams if one can be rearranged into the other, using every letter exactly once. Put the strings into groups so that each group holds all the strings that are anagrams of each other. The groups, and the strings inside them, can be in any order.

Example 1:
Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]
Explanation: "act" and "cat" share the same letters, as do "pots", "tops" and "stop". "hat" has no partner.

Example 2:
Input: strs = ["x"]
Output: [["x"]]
Explanation: A single string forms its own group.

Example 3:
Input: strs = [""]
Output: [[""]]
Explanation: An empty string is a valid string too.

Constraints:
- 1 <= len(strs) <= 1,000
- 0 <= len(strs[i]) <= 100
- Strings contain lowercase English letters only
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
