"""
Design Add And Search Words Data Structure (Medium)

Design a class WordDictionary with these methods:

- addWord(word) stores word.
- search(word) returns True if any stored word matches word. Each "." in the search string matches exactly one letter of any kind, and the lengths must be equal.

Example 1:
w = WordDictionary()
w.addWord("day")
w.addWord("bay")
w.addWord("may")
w.search("say")   ->  False
w.search("day")   ->  True
w.search(".ay")   ->  True
w.search("b..")   ->  True
w.search("..")    ->  False
Explanation: ".." is False because every stored word has three letters, and "." matches exactly one.

Constraints:
- 1 <= len(word) <= 20
- addWord receives lowercase letters only
- search receives lowercase letters and "."
"""

class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            node = node.setdefault(c, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return "$" in node
            if word[i] == ".":
                return any(k != "$" and dfs(v, i + 1) for k, v in node.items())
            return word[i] in node and dfs(node[word[i]], i + 1)
        return dfs(self.root, 0)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
