"""
Maximum Product Subarray (Medium)

Return the largest product of any contiguous, non-empty run of values in nums.

Example 1:
Input: nums = [1, 2, -3, 4]
Output: 4
Explanation: The run [4] beats [1, 2].

Example 2:
Input: nums = [-2, -1]
Output: 2

Example 3:
Input: nums = [-2, 0, -1]
Output: 0

Constraints:
- 1 <= len(nums) <= 1,000
"""

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
