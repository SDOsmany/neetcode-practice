"""
Partition Labels (Medium)

Split s into as many pieces as possible so that each letter appears in only one piece. Return the piece lengths in order.

Example 1:
Input: s = "xyxxyzbzbbisl"
Output: [5, 5, 1, 1, 1]
Explanation: "xyxxy", "zbzbb", "i", "s", "l".

Example 2:
Input: s = "abcabc"
Output: [6]

Example 3:
Input: s = "abc"
Output: [1, 1, 1]

Constraints:
- 1 <= len(s) <= 100
- Lowercase letters only
"""

class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
