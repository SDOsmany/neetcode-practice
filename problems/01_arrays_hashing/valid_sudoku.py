"""
Valid Sudoku (Medium)

board is a 9 x 9 Sudoku board using "1" to "9" and "." for empty. Return True if no digit repeats in any row, any column or any of the nine 3 x 3 boxes. You only check the filled cells: the board doesn't need to be solvable.

Example 1:
A board whose only filled cells are "5" at row 0 column 0 and "5" at row 4 column 4  ->  True
Explanation: They share no row, column or box.

Example 2:
A board with "5" at row 0 column 0 and "5" at row 1 column 1  ->  False
Explanation: Both are in the top-left 3 x 3 box.

Constraints:
- board is always 9 x 9
- Cells hold "1" to "9" or "."
"""

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
