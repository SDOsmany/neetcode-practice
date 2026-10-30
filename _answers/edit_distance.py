"""
Edit Distance (Medium)

Return the fewest operations needed to turn word1 into word2. An operation inserts, deletes or replaces one character.

Example 1:
Input: word1 = "monkeys", word2 = "money"
Output: 2
Explanation: Delete "k" and then "s": monkeys -> moneys -> money.

Example 2:
Input: word1 = "neatcdee", word2 = "neetcode"
Output: 3

Example 3:
Input: word1 = "", word2 = "abc"
Output: 3

Constraints:
- 0 <= len(word1), len(word2) <= 500
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        row = list(range(len(word2) + 1))
        for i, a in enumerate(word1, 1):
            diag, row[0] = row[0], i
            for j, b in enumerate(word2, 1):
                diag, row[j] = row[j], diag if a == b else 1 + min(diag, row[j], row[j - 1])
        return row[-1]


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
