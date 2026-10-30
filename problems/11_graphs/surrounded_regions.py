"""
Surrounded Regions (Medium)

board holds "X" and "O". A region of connected "O" cells, up, down, left or right, is captured if none of its cells touch the board's edge. Turn every captured "O" into "X". Change board in place and return nothing.

Example 1:
Input: board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "O", "O", "X"], ["X", "X", "X", "O"]]
Output: [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "O"]]
Explanation: The middle region is captured, and the corner O touches the edge.

Example 2:
Input: board = [["O", "O"], ["O", "X"]]
Output: [["O", "O"], ["O", "X"]]

Example 3:
Input: board = [["X", "X", "X"], ["X", "O", "X"], ["X", "X", "X"]]
Output: [["X", "X", "X"], ["X", "X", "X"], ["X", "X", "X"]]

Constraints:
- 1 <= rows, columns <= 100
"""

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
