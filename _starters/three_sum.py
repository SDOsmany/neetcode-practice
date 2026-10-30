"""
3Sum (Medium)

Return every distinct triplet of values from nums, at three different positions, that adds up to 0. No triplet may appear twice, and any output order is fine.

Example 1:
Input: nums = [-1, 0, 1, 2, -1, -4]
Output: [[-1, -1, 2], [-1, 0, 1]]
Explanation: Those are the only two distinct triplets that add up to 0.

Example 2:
Input: nums = [0, 1, 1]
Output: []

Example 3:
Input: nums = [0, 0, 0, 0]
Output: [[0, 0, 0]]
Explanation: Each distinct triplet appears once.

Constraints:
- 3 <= len(nums) <= 1,000
"""

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
