"""
Partition Equal Subset Sum (Medium)

Return True if nums can be split into two groups with the same sum.

Example 1:
Input: nums = [1, 2, 3, 4]
Output: True
Explanation: [1, 4] and [2, 3] both add up to 5.

Example 2:
Input: nums = [1, 2, 3, 4, 5]
Output: False
Explanation: The total is odd.

Example 3:
Input: nums = [1, 2, 5]
Output: False

Constraints:
- 1 <= len(nums) <= 200
- 1 <= nums[i] <= 100
"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        reachable = {0}
        for n in nums:
            reachable |= {x + n for x in reachable}
        return total // 2 in reachable


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
