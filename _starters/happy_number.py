"""
Happy Number (Easy)

Repeatedly replace n with the sum of the squares of its digits. Return True if this reaches 1. If it loops forever without reaching 1, return False.

Example 1:
Input: n = 100
Output: True
Explanation: 1 + 0 + 0 = 1.

Example 2:
Input: n = 101
Output: False

Example 3:
Input: n = 19
Output: True
Explanation: 19 -> 82 -> 68 -> 100 -> 1.

Constraints:
- 1 <= n <= 1,000,000
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
