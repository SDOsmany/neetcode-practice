"""
Top K Frequent Elements (Medium)

Return the k values that appear most often in nums, in any order. The answer is guaranteed to be unique.

Example 1:
Input: nums = [1, 2, 2, 3, 3, 3], k = 2
Output: [2, 3]
Explanation: 3 appears three times and 2 appears twice.

Example 2:
Input: nums = [7, 7], k = 1
Output: [7]

Example 3:
Input: nums = [4, 1, 4, 2, 2, 4], k = 2
Output: [4, 2]

Constraints:
- 1 <= k <= number of distinct values
- 1 <= len(nums) <= 10,000
"""

from collections import Counter

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        for n, c in Counter(nums).items():
            buckets[c].append(n)
        res = []
        for c in range(len(nums), 0, -1):
            res += buckets[c]
            if len(res) >= k:
                return res[:k]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
