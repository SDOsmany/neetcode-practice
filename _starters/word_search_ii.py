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
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
