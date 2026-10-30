"""
Palindrome Partitioning (Medium)

Split s into pieces so that every piece is a palindrome. Return every possible split, in any order.

Example 1:
Input: s = "aab"
Output: [["a", "a", "b"], ["aa", "b"]]

Example 2:
Input: s = "a"
Output: [["a"]]

Example 3:
Input: s = "aba"
Output: [["a", "b", "a"], ["aba"]]

Constraints:
- 1 <= len(s) <= 16
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
