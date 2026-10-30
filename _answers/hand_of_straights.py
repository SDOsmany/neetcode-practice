"""
Hand of Straights (Medium)

Return True if the cards in hand can be arranged into groups of exactly groupSize cards, where each group is a run of consecutive values.

Example 1:
Input: hand = [1, 2, 4, 2, 3, 5, 3, 4], groupSize = 4
Output: True
Explanation: [1, 2, 3, 4] and [2, 3, 4, 5].

Example 2:
Input: hand = [1, 2, 3, 3, 4, 5, 6, 7], groupSize = 4
Output: False

Example 3:
Input: hand = [1, 2, 3], groupSize = 2
Output: False
Explanation: 3 cards can't be split into groups of 2.

Constraints:
- 1 <= len(hand) <= 1,000
- 1 <= groupSize <= len(hand)
"""

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        count = Counter(hand)
        for start in sorted(count):
            need = count[start]
            if need:
                for v in range(start, start + groupSize):
                    if count[v] < need:
                        return False
                    count[v] -= need
        return True


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
