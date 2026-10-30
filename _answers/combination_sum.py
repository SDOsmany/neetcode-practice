"""
Combination Sum (Medium)

nums contains distinct positive integers and target is a positive integer. Return every unique combination of values from nums that adds up to target. Each value may be used any number of times. Two combinations are the same if they use the same values the same number of times, regardless of order. Any output order is fine.

Example 1:
Input: nums = [2, 5, 6, 9], target = 9
Output: [[2, 2, 5], [9]]
Explanation: 2 + 2 + 5 = 9, and 9 on its own also works.

Example 2:
Input: nums = [3, 4, 5], target = 16
Output: [[3, 3, 3, 3, 4], [3, 3, 5, 5], [3, 4, 4, 5], [4, 4, 4, 4]]
Explanation: All four combinations add up to 16.

Example 3:
Input: nums = [3], target = 5
Output: []
Explanation: No number of 3s adds up to 5.

Constraints:
- 1 <= len(nums) <= 20
- 2 <= nums[i] <= 30
- 1 <= target <= 40
"""

class Solution:
    def combinationSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        cur = []
        def dfs(start, left):
            if left == 0:
                res.append(cur[:])
                return
            for i in range(start, len(nums)):
                if nums[i] <= left:
                    cur.append(nums[i])
                    dfs(i, left - nums[i])
                    cur.pop()
        dfs(0, target)
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
