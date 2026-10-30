"""
Word Search II (Hard)

board is a grid of letters. Return every word from words that can be traced through the grid. A word is traced through horizontally or vertically adjacent cells, and one word can't reuse a cell. Any output order is fine.

Example 1:
Input: board = [["a", "b", "c", "d"], ["s", "a", "a", "t"], ["a", "c", "k", "e"], ["a", "c", "d", "n"]], words = ["bat", "cat", "back", "backend", "stack"]
Output: ["cat", "back", "backend"]

Example 2:
Input: board = [["x", "o"], ["x", "o"]], words = ["xoxo"]
Output: []

Example 3:
Input: board = [["a", "a"]], words = ["aaa"]
Output: []
Explanation: A cell can't be used twice.

Constraints:
- 1 <= rows, columns <= 12
- 1 <= len(words) <= 1,000
"""

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = {}
        for w in words:
            node = root
            for c in w:
                node = node.setdefault(c, {})
            node["$"] = w
        rows, cols = len(board), len(board[0])
        found = set()
        def dfs(r, c, node):
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] not in node:
                return
            ch = board[r][c]
            nxt = node[ch]
            if "$" in nxt:
                found.add(nxt["$"])
            board[r][c] = "#"
            for x, y in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                dfs(x, y, nxt)
            board[r][c] = ch
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        return list(found)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
