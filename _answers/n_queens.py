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
        cols, up, down = set(), set(), set()
        placed, res = [], []
        def dfs(r):
            if r == n:
                res.append(["." * c + "Q" + "." * (n - c - 1) for c in placed])
                return
            for c in range(n):
                if c in cols or r + c in up or r - c in down:
                    continue
                cols.add(c); up.add(r + c); down.add(r - c); placed.append(c)
                dfs(r + 1)
                cols.remove(c); up.remove(r + c); down.remove(r - c); placed.pop()
        dfs(0)
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
