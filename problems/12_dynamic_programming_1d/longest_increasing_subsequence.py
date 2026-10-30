"""
Longest Increasing Subsequence (Medium)

Return the length of the longest strictly increasing subsequence of nums. A subsequence keeps the original order but can skip values.

Example 1:
Input: nums = [9, 1, 4, 2, 3, 3, 7]
Output: 4
Explanation: 1, 2, 3, 7.

Example 2:
Input: nums = [0, 3, 1, 3, 2, 3]
Output: 4

Example 3:
Input: nums = [5, 5, 5]
Output: 1
Explanation: The values must strictly increase.

Constraints:
- 1 <= len(nums) <= 1,000
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
