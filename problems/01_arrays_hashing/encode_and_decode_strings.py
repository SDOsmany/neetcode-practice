"""
Encode and Decode Strings (Medium)

Design two methods. encode(strs) turns a list of strings into one string. decode(s) turns that string back into the original list. Strings may contain any characters, including whatever separator you might pick.

Example 1:
s.decode(s.encode(["neet", "code"]))  ->  ["neet", "code"]
Explanation: The list comes back unchanged.

Example 2:
s.decode(s.encode(["a#b", "", "3#x"]))  ->  ["a#b", "", "3#x"]
Explanation: Separators and empty strings have to survive.

Constraints:
- 0 <= len(strs) <= 100
- 0 <= len(strs[i]) <= 200
"""

class Solution:
    def encode(self, strs: list[str]) -> str:
        pass

    def decode(self, s: str) -> list[str]:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
