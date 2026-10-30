"""
Binary Search (Easy)

You're given an array nums of distinct integers sorted in ascending order, and an integer target. Return the index of target, or -1 if it isn't in the array. Your solution must run in O(log n) time.

Example 1:
Input: nums = [-1, 0, 2, 4, 6, 8], target = 4
Output: 3
Explanation: nums[3] is 4.

Example 2:
Input: nums = [-1, 0, 2, 4, 6, 8], target = 3
Output: -1
Explanation: 3 isn't in the array.

Example 3:
Input: nums = [5], target = 5
Output: 0
Explanation: A single element can still match.

Constraints:
- 0 <= len(nums) <= 10,000
- All values are distinct
- nums is sorted in ascending order
"""

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
