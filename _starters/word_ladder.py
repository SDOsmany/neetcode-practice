"""
Word Ladder (Hard)

Transform beginWord into endWord by changing one letter at a time. Every word after beginWord must be in wordList. Return the number of words in the shortest such sequence, counting both ends, or 0 if there is none.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
Output: 5
Explanation: hit -> hot -> dot -> dog -> cog.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"]
Output: 0
Explanation: "cog" isn't in the list.

Example 3:
Input: beginWord = "a", endWord = "c", wordList = ["a", "b", "c"]
Output: 2

Constraints:
- All words have the same length
- 1 <= len(wordList) <= 1,000
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
