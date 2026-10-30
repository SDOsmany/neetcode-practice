"""
Implement Trie (Prefix Tree) (Medium)

A trie, or prefix tree, stores words so they can be looked up letter by letter. Design a class PrefixTree with these methods:

- insert(word) stores word.
- search(word) returns True only if that exact word was inserted.
- startsWith(prefix) returns True if any inserted word begins with prefix.

Example 1:
t = PrefixTree()
t.insert("dog")
t.search("dog")    ->  True
t.search("do")     ->  False
t.startsWith("do") ->  True
t.insert("do")
t.search("do")     ->  True
Explanation: "do" is only a prefix until it is inserted as a word of its own.

Constraints:
- 1 <= len(word), len(prefix) <= 1,000
- Strings contain lowercase English letters only
"""

class PrefixTree:
    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
