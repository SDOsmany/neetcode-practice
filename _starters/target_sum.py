"""
Target Sum (Medium)

Put a + or - in front of every value in nums. Return how many ways of doing this add up to target.

Example 1:
Input: nums = [2, 2, 2], target = 2
Output: 3
Explanation: Two plus signs and one minus, in three possible positions.

Example 2:
Input: nums = [1], target = 2
Output: 0

Example 3:
Input: nums = [1, 1, 1, 1, 1], target = 3
Output: 5

Constraints:
- 1 <= len(nums) <= 20
"""

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
