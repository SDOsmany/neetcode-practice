"""
Largest Rectangle In Histogram (Hard)

heights[i] is the height of a histogram bar of width 1. Return the area of the largest rectangle that fits entirely inside the bars.

Example 1:
Input: heights = [7, 1, 7, 2, 2, 4]
Output: 8
Explanation: The last four bars support height 2 across width 4.

Example 2:
Input: heights = [1, 3, 7]
Output: 7
Explanation: The bar of height 7 alone gives 7.

Example 3:
Input: heights = [2, 1, 5, 6, 2, 3]
Output: 10
Explanation: Bars 5 and 6 support height 5 across width 2.

Constraints:
- 1 <= len(heights) <= 1,000
- 0 <= heights[i] <= 1,000
"""

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        best = 0
        for i, h in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > h:
                j, top = stack.pop()
                best = max(best, top * (i - j))
                start = j
            stack.append((start, h))
        return best


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
