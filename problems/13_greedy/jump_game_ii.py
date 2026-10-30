"""
Jump Game II (Medium)

You start at index 0. nums[i] is the longest jump you can make from index i, and you may also jump any shorter distance. The last index is always reachable. Return the fewest jumps needed to reach it.

Example 1:
Input: nums = [2, 4, 1, 1, 1, 1]
Output: 2
Explanation: Jump 0 -> 1, then 1 -> 5.

Example 2:
Input: nums = [2, 1, 2, 1, 0]
Output: 2
Explanation: Jump 0 -> 2, then 2 -> 4.

Example 3:
Input: nums = [0]
Output: 0
Explanation: You're already there, so no jumps are needed.

Constraints:
- 1 <= len(nums) <= 1,000
- 0 <= nums[i] <= 100
- The last index is always reachable
"""

class Solution:
    def jump(self, nums: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
