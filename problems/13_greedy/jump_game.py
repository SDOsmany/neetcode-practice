"""
Jump Game (Medium)

You start at index 0. nums[i] is the longest jump you can make from index i, and you may also jump any shorter distance. Return True if you can reach the last index, otherwise False.

Example 1:
Input: nums = [1, 2, 0, 1, 0]
Output: True
Explanation: Jump 0 -> 1 -> 3 -> 4.

Example 2:
Input: nums = [1, 2, 1, 0, 1]
Output: False
Explanation: Every route lands on index 3, where the jump length is 0.

Example 3:
Input: nums = [0]
Output: True
Explanation: You're already at the last index.

Constraints:
- 1 <= len(nums) <= 1,000
- 0 <= nums[i] <= 1,000
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
