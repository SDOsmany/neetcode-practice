"""
Two Sum (Easy)

You're given an integer array nums and an integer target. Find the two different positions whose values add up to target and return them as [i, j] with i < j. Exactly one valid pair exists in every input. You can't use the same position twice, though two positions may hold equal values.

Example 1:
Input: nums = [3, 4, 5, 6], target = 7
Output: [0, 1]
Explanation: nums[0] + nums[1] = 3 + 4 = 7.

Example 2:
Input: nums = [4, 5, 6], target = 10
Output: [0, 2]
Explanation: nums[0] + nums[2] = 4 + 6 = 10.

Example 3:
Input: nums = [5, 5], target = 10
Output: [0, 1]
Explanation: Different positions can hold the same value.

Constraints:
- 2 <= len(nums) <= 10,000
- Values and target can be negative
- Exactly one answer exists
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
