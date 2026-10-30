"""
Missing Number (Easy)

nums holds n distinct values from the range 0 to n, so exactly one is missing. Return it using O(1) extra space.

Example 1:
Input: nums = [1, 2, 3]
Output: 0

Example 2:
Input: nums = [0, 2]
Output: 1

Example 3:
Input: nums = [0, 1]
Output: 2

Constraints:
- 1 <= len(nums) <= 10,000
"""

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
