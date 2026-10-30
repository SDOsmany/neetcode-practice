"""
Subsets II (Medium)

nums may contain duplicates. Return every distinct subset, in any order.

Example 1:
Input: nums = [1, 2, 1]
Output: [[], [1], [1, 1], [1, 1, 2], [1, 2], [2]]
Explanation: [1, 2] appears once even though there are two 1s.

Example 2:
Input: nums = [7, 7]
Output: [[], [7], [7, 7]]

Constraints:
- 1 <= len(nums) <= 10
"""

class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        res, cur = [], []
        def dfs(start):
            res.append(cur[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1)
                cur.pop()
        dfs(0)
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
