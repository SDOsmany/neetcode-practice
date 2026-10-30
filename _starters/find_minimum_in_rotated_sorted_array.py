"""
Find Minimum In Rotated Sorted Array (Medium)

A sorted array of distinct integers was rotated at an unknown point. Return its smallest value in O(log n) time.

Example 1:
Input: nums = [3, 4, 5, 6, 1, 2]
Output: 1

Example 2:
Input: nums = [4, 5, 0, 1, 2, 3]
Output: 0

Example 3:
Input: nums = [4, 5, 6, 7]
Output: 4
Explanation: A full rotation leaves the array in order.

Constraints:
- 1 <= len(nums) <= 1,000
- All values are distinct
"""

class Solution:
    def findMin(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
