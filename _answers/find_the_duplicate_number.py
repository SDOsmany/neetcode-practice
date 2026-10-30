"""
Find The Duplicate Number (Medium)

nums has n + 1 values, each between 1 and n, and exactly one value is repeated, possibly several times. Return it without changing nums, using only O(1) extra space.

Example 1:
Input: nums = [1, 2, 3, 2, 2]
Output: 2

Example 2:
Input: nums = [1, 2, 3, 4, 4]
Output: 4

Example 3:
Input: nums = [3, 1, 3, 4, 2]
Output: 3

Constraints:
- 2 <= len(nums) <= 10,000
- 1 <= nums[i] <= len(nums) - 1
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        slow = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
        return slow


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
