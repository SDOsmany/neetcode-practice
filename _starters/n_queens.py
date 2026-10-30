"""
N Queens (Hard)

Place n queens on an n x n chess board so that no two share a row, column or diagonal. Return every solution, in any order. Each solution is a list of n strings, with "Q" for a queen and "." for empty.

Example 1:
Input: n = 4
Output: [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
Explanation: There are exactly two arrangements on a 4 x 4 board.

Example 2:
Input: n = 1
Output: [["Q"]]

Example 3:
Input: n = 2
Output: []
Explanation: Two queens on a 2 x 2 board always attack each other.

Constraints:
- 1 <= n <= 8
"""

class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
