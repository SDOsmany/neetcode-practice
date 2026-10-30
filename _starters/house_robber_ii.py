"""
House Robber II (Medium)

Same as House Robber, except the houses are in a circle, so the first and last houses are next to each other. Return the most money you can take without robbing two adjacent houses.

Example 1:
Input: nums = [3, 4, 3]
Output: 4
Explanation: Houses 0 and 2 are adjacent, so you can't take both.

Example 2:
Input: nums = [2, 9, 8, 3, 6]
Output: 15
Explanation: Houses 1 and 4 give 9 + 6 = 15.

Example 3:
Input: nums = [7]
Output: 7

Constraints:
- 1 <= len(nums) <= 100
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
