"""
Two Sum II - Input Array Is Sorted (Medium)

You're given an integer array numbers sorted in ascending order and an integer target. Find the two numbers that add up to target and return their positions counted from 1, as [i, j] with i < j. Exactly one valid pair exists. Your solution should use only O(1) extra space.

Example 1:
Input: numbers = [1, 2, 3, 4], target = 3
Output: [1, 2]
Explanation: 1 + 2 = 3, and those values are in positions 1 and 2.

Example 2:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: 2 + 7 = 9.

Example 3:
Input: numbers = [-3, -1, 0, 5], target = 4
Output: [2, 4]
Explanation: -1 + 5 = 4.

Constraints:
- 2 <= len(numbers) <= 1,000
- numbers is sorted in ascending order
- Exactly one answer exists
"""

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
