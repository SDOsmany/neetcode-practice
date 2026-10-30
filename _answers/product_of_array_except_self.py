"""
Product of Array Except Self (Medium)

Return an array where result[i] is the product of every value in nums except nums[i]. Solve it in O(n) time without using division.

Example 1:
Input: nums = [1, 2, 4, 6]
Output: [48, 24, 12, 8]
Explanation: For index 1: 1 * 4 * 6 = 24.

Example 2:
Input: nums = [-1, 0, 1, 2, 3]
Output: [0, -6, 0, 0, 0]
Explanation: Only the slot holding the 0 avoids multiplying by 0.

Example 3:
Input: nums = [2, 3]
Output: [3, 2]

Constraints:
- 2 <= len(nums) <= 1,000
- Products fit in a normal integer
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        left = 1
        for i, n in enumerate(nums):
            res[i] = left
            left *= n
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
