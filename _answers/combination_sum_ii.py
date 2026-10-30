"""
Combination Sum II (Medium)

candidates may contain duplicates. Return every unique combination that adds up to target, where each position can be used at most once. Any output order is fine.

Example 1:
Input: candidates = [9, 2, 2, 4, 6, 1, 5], target = 8
Output: [[1, 2, 5], [2, 2, 4], [2, 6]]
Explanation: The two 2s can be used together, but each combination appears once.

Example 2:
Input: candidates = [1, 2, 3, 4, 5], target = 7
Output: [[1, 2, 4], [2, 5], [3, 4]]

Example 3:
Input: candidates = [3], target = 1
Output: []

Constraints:
- 1 <= len(candidates) <= 100
- 1 <= target <= 30
"""

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        nums = sorted(candidates)
        res, cur = [], []
        def dfs(start, left):
            if left == 0:
                res.append(cur[:])
                return
            for i in range(start, len(nums)):
                if nums[i] > left:
                    break
                if i > start and nums[i] == nums[i - 1]:
                    continue
                cur.append(nums[i])
                dfs(i + 1, left - nums[i])
                cur.pop()
        dfs(0, target)
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
