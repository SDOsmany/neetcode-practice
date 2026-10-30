"""
Letter Combinations of a Phone Number (Medium)

digits holds characters from "2" to "9". Each maps to letters as on a phone keypad: 2 is abc, 3 is def, 4 is ghi, 5 is jkl, 6 is mno, 7 is pqrs, 8 is tuv and 9 is wxyz. Return every string the digits could spell, in any order. An empty input gives an empty list.

Example 1:
Input: digits = "34"
Output: ["dg", "dh", "di", "eg", "eh", "ei", "fg", "fh", "fi"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "7"
Output: ["p", "q", "r", "s"]

Constraints:
- 0 <= len(digits) <= 4
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        keys = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        if not digits:
            return []
        res = [""]
        for d in digits:
            res = [word + c for word in res for c in keys[d]]
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
