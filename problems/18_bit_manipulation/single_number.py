"""
Single Number (Easy)

Every value in nums appears twice, except one that appears once. Return that value using O(1) extra space.

Example 1:
Input: nums = [3, 2, 3]
Output: 2

Example 2:
Input: nums = [7, 6, 6, 7, 8]
Output: 8

Example 3:
Input: nums = [-1]
Output: -1

Constraints:
- 1 <= len(nums) <= 10,000
"""

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
