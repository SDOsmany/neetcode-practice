"""
Alien Dictionary (Hard)

words is sorted in an alien language that uses lowercase letters in an unknown order. Return a string of all the letters used, in an order consistent with that sorting. Return "" if no order is possible. The tests only use inputs that have one valid order.

Example 1:
Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
Output: "wertf"
Explanation: t comes before f, w before e, r before t, and e before r.

Example 2:
Input: words = ["z", "x", "z"]
Output: ""
Explanation: z can't be both before and after x.

Example 3:
Input: words = ["abc", "ab"]
Output: ""
Explanation: A word can't come after its own prefix.

Constraints:
- 1 <= len(words) <= 100
- Lowercase letters only
"""

from collections import deque

class Solution:
    def alienOrder(self, words: list[str]) -> str:
        after = {c: set() for w in words for c in w}
        waiting = {c: 0 for c in after}
        for a, b in zip(words, words[1:]):
            for x, y in zip(a, b):
                if x != y:
                    if y not in after[x]:
                        after[x].add(y)
                        waiting[y] += 1
                    break
            else:
                if len(a) > len(b):
                    return ""
        q = deque(c for c in after if waiting[c] == 0)
        order = []
        while q:
            c = q.popleft()
            order.append(c)
            for y in after[c]:
                waiting[y] -= 1
                if waiting[y] == 0:
                    q.append(y)
        return "".join(order) if len(order) == len(after) else ""


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
