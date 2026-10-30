"""
House Robber (Medium)

nums[i] is the money in house i on a street. You can rob any set of houses, as long as no two of them are next to each other. Return the most money you can take.

Example 1:
Input: nums = [1, 1, 3, 3]
Output: 4
Explanation: Rob a 1 and a non-adjacent 3, such as houses 0 and 2.

Example 2:
Input: nums = [2, 9, 8, 3, 6]
Output: 16
Explanation: Rob houses 0, 2 and 4: 2 + 8 + 6. Taking the 9 gives at most 9 + 6 = 15 here, or 9 + 3 = 12.

Example 3:
Input: nums = [2, 1, 1, 2]
Output: 4
Explanation: Rob both ends: the best choice can skip two houses in a row.

Constraints:
- 0 <= len(nums) <= 100
- 0 <= nums[i] <= 400
"""

class Solution:
    def rob(self, nums: list[int]) -> int:
        skip, take = 0, 0
        for n in nums:
            skip, take = take, max(take, skip + n)
        return take


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
