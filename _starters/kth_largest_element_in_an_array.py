"""
Kth Largest Element In An Array (Medium)

Return the kth largest value in nums, counting duplicates separately. Try to do better than sorting the whole array.

Example 1:
Input: nums = [2, 3, 1, 5, 4], k = 2
Output: 4

Example 2:
Input: nums = [2, 3, 1, 1, 5, 5, 4], k = 3
Output: 4
Explanation: In descending order: 5, 5, 4, ...

Example 3:
Input: nums = [1], k = 1
Output: 1

Constraints:
- 1 <= k <= len(nums) <= 10,000
"""

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
