"""
Pacific Atlantic Water Flow (Medium)

heights is a map of land heights. The Pacific touches the top and left edges, and the Atlantic touches the bottom and right edges. Water flows from a cell to a neighbor that is the same height or lower, up, down, left or right. Return every [r, c] from which water can reach both oceans, in any order.

Example 1:
Input: heights = [[4, 2, 7, 3, 4], [7, 4, 6, 4, 7], [6, 3, 5, 3, 6]]
Output: [[0, 2], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [2, 0]]

Example 2:
Input: heights = [[1], [1]]
Output: [[0, 0], [1, 0]]

Example 3:
Input: heights = [[1, 2], [4, 3]]
Output: [[0, 1], [1, 0], [1, 1]]

Constraints:
- 1 <= rows, columns <= 100
"""

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])
        def reach(starts):
            seen = set(starts)
            stack = list(starts)
            while stack:
                r, c = stack.pop()
                for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= x < rows and 0 <= y < cols and (x, y) not in seen and heights[x][y] >= heights[r][c]:
                        seen.add((x, y))
                        stack.append((x, y))
            return seen
        pacific = reach([(0, c) for c in range(cols)] + [(r, 0) for r in range(rows)])
        atlantic = reach([(rows - 1, c) for c in range(cols)] + [(r, cols - 1) for r in range(rows)])
        return [list(p) for p in pacific & atlantic]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
