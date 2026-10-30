"""
Longest Consecutive Sequence (Medium)

Return the length of the longest run of consecutive integers that can be formed from values in nums, such as 2, 3, 4, 5. The values can be anywhere in the array. Your solution should run in O(n) time.

Example 1:
Input: nums = [2, 20, 4, 10, 3, 4, 5]
Output: 4
Explanation: The run is 2, 3, 4, 5.

Example 2:
Input: nums = [0, 3, 2, 5, 4, 6, 1, 1]
Output: 7
Explanation: The run is 0 through 6. Duplicates don't add length.

Example 3:
Input: nums = []
Output: 0

Constraints:
- 0 <= len(nums) <= 1,000
"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        values = set(nums)
        best = 0
        for n in values:
            if n - 1 not in values:
                end = n
                while end + 1 in values:
                    end += 1
                best = max(best, end - n + 1)
        return best


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
