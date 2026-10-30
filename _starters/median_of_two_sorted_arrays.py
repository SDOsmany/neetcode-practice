"""
Median of Two Sorted Arrays (Hard)

nums1 and nums2 are sorted ascending. Return the median of all their values combined. If the total count is even, the median is the average of the two middle values. Aim for O(log(m + n)) time.

Example 1:
Input: nums1 = [1, 2], nums2 = [3]
Output: 2.0
Explanation: Combined, the values are 1, 2, 3, and the middle one is 2.

Example 2:
Input: nums1 = [1, 3], nums2 = [2, 4]
Output: 2.5
Explanation: The middle two values are 2 and 3.

Example 3:
Input: nums1 = [], nums2 = [1]
Output: 1.0

Constraints:
- 0 <= len(nums1), len(nums2) <= 1,000
- At least one array has a value
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
