"""
Maximum Subarray (Medium)

Find the contiguous, non-empty run of values in nums with the largest sum, and return that sum. You must include at least one value, even if they're all negative.

Example 1:
Input: nums = [2, -3, 4, -2, 2, 1, -1, 4]
Output: 8
Explanation: The run [4, -2, 2, 1, -1, 4] adds up to 8.

Example 2:
Input: nums = [-1]
Output: -1
Explanation: You have to take at least one value.

Example 3:
Input: nums = [-3, -2, -5]
Output: -2
Explanation: With only negatives, the best run is the largest single value.

Constraints:
- 1 <= len(nums) <= 100,000
- -10,000 <= nums[i] <= 10,000
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
