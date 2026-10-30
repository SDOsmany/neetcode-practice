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
        return "".join(f"{len(w)}#{w}" for w in strs)

    def decode(self, s: str) -> list[str]:
        res, i = [], 0
        while i < len(s):
            j = s.index("#", i)
            size = int(s[i:j])
            res.append(s[j + 1:j + 1 + size])
            i = j + 1 + size
        return res


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
