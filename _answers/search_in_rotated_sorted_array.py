"""
Search In Rotated Sorted Array (Medium)

A sorted array of distinct integers was rotated at an unknown point, so that a run from the end moved to the front. For example, [1, 2, 3, 4, 5, 6] could become [3, 4, 5, 6, 1, 2]. Return the index of target, or -1 if it's missing. Your solution must run in O(log n) time.

Example 1:
Input: nums = [3, 4, 5, 6, 1, 2], target = 1
Output: 4
Explanation: nums[4] is 1.

Example 2:
Input: nums = [3, 5, 6, 0, 1, 2], target = 4
Output: -1
Explanation: 4 isn't in the array.

Example 3:
Input: nums = [1], target = 1
Output: 0
Explanation: A one-element array isn't visibly rotated at all.

Constraints:
- 1 <= len(nums) <= 1,000
- All values are distinct
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
