"""
Word Search (Medium)

board is a grid of letters. Return True if word can be traced through horizontally or vertically adjacent cells, without using a cell twice.

Example 1:
Input: board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], word = "CAT"
Output: True

Example 2:
Input: board = [["A", "B", "C", "D"], ["S", "A", "A", "T"], ["A", "C", "A", "E"]], word = "BAT"
Output: False

Example 3:
Input: board = [["A", "A"]], word = "AAA"
Output: False
Explanation: A cell can't be used twice.

Constraints:
- 1 <= rows, columns <= 6
- 1 <= len(word) <= 15
"""

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            found = any(dfs(x, y, i + 1) for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)))
            board[r][c] = word[i]
            return found
        return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
