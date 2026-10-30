"""
Subsets (Medium)

nums contains distinct integers. Return every possible subset, including the empty set and nums itself. No subset may appear twice. The subsets, and the values inside them, can be in any order.

Example 1:
Input: nums = [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
Explanation: Each value is either in or out, so 3 values give 2^3 = 8 subsets.

Example 2:
Input: nums = [7]
Output: [[], [7]]
Explanation: One value gives 2 subsets.

Constraints:
- 1 <= len(nums) <= 10
- All values are distinct
"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
