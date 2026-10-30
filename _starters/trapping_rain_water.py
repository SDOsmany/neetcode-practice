"""
Trapping Rain Water (Hard)

height[i] is the height of a bar of width 1. After rain, water collects between the bars. Return the total units of water held.

Example 1:
Input: height = [0, 2, 0, 3, 1, 0, 1, 3, 2, 1]
Output: 9
Explanation: Water fills the gaps between the bars of height 2 and 3, and between the two bars of height 3.

Example 2:
Input: height = [3, 0, 2]
Output: 2
Explanation: Only the middle cell holds water, up to level 2.

Example 3:
Input: height = [1, 2, 3]
Output: 0

Constraints:
- 1 <= len(height) <= 1,000
- 0 <= height[i] <= 1,000
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
