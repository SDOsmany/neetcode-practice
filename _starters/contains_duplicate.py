"""
Contains Duplicate (Easy)

You're given an integer array nums. Return True if at least one value appears two or more times anywhere in the array. Return False if every value is distinct.

Example 1:
Input: nums = [1, 2, 3, 1]
Output: True
Explanation: The value 1 appears at index 0 and index 3.

Example 2:
Input: nums = [1, 2, 3, 4]
Output: False
Explanation: All four values are different.

Example 3:
Input: nums = []
Output: False
Explanation: An empty array has no repeats.

Constraints:
- 0 <= len(nums) <= 100,000
- -1,000,000,000 <= nums[i] <= 1,000,000,000
"""

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
