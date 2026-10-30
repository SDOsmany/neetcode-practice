"""
Permutations (Medium)

nums contains distinct integers. Return every possible ordering of them, in any order.

Example 1:
Input: nums = [1, 2, 3]
Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
Explanation: 3 values have 3! = 6 orderings.

Example 2:
Input: nums = [7]
Output: [[7]]

Constraints:
- 1 <= len(nums) <= 6
- All values are distinct
"""

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res, cur, used = [], [], set()
        def dfs():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            for n in nums:
                if n not in used:
                    used.add(n)
                    cur.append(n)
                    dfs()
                    cur.pop()
                    used.remove(n)
        dfs()
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
