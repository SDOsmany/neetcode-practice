"""
Sliding Window Maximum (Hard)

A window of size k slides from the start of nums to the end, one position at a time. Return an array holding the largest value in each window position.

Example 1:
Input: nums = [1, 2, 1, 0, 4, 2, 6], k = 3
Output: [2, 2, 4, 4, 6]
Explanation: The first window [1, 2, 1] has maximum 2, and the last [4, 2, 6] has maximum 6.

Example 2:
Input: nums = [5], k = 1
Output: [5]

Example 3:
Input: nums = [9, 8, 7], k = 2
Output: [9, 8]

Constraints:
- 1 <= k <= len(nums) <= 100,000
"""

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
