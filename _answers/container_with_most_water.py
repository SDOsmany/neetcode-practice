"""
Container With Most Water (Medium)

heights[i] is the height of a vertical bar standing at position i. Choose two bars. Together with the ground they form a container, whose water level can't rise above the shorter bar. The area it holds is (distance between the bars) * (height of the shorter bar). Return the largest area possible.

Example 1:
Input: heights = [1, 7, 2, 5, 4, 7, 3, 6]
Output: 36
Explanation: Use positions 1 and 7, with heights 7 and 6. The width is 6 and the shorter bar is 6, so the area is 36.

Example 2:
Input: heights = [2, 2, 2]
Output: 4
Explanation: Use the two outer bars: width 2 * height 2 = 4.

Example 3:
Input: heights = [1, 1]
Output: 1
Explanation: There's only one choice: width 1 * height 1.

Constraints:
- 2 <= len(heights) <= 1,000
- 0 <= heights[i] <= 1,000
"""

class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        best = 0
        while l < r:
            best = max(best, (r - l) * min(heights[l], heights[r]))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return best


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
