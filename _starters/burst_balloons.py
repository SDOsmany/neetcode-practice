"""
Burst Balloons (Hard)

nums[i] is the value of balloon i. Bursting a balloon earns (left neighbor) * (its value) * (right neighbor), where missing neighbors count as 1, and the neighbors change as balloons disappear. Return the most coins you can earn by bursting them all.

Example 1:
Input: nums = [4, 2, 3, 7]
Output: 143
Explanation: Burst 2, then 3, then 4, then 7: 24 + 84 + 28 + 7.

Example 2:
Input: nums = [3, 1, 5, 8]
Output: 167

Example 3:
Input: nums = [5]
Output: 5

Constraints:
- 1 <= len(nums) <= 300
"""

class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
