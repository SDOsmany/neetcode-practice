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
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
