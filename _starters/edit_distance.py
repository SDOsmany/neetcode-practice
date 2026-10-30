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
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
