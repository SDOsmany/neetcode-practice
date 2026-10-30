"""
Koko Eating Bananas (Medium)

piles[i] is the number of bananas in pile i. Koko chooses a fixed eating speed of k bananas per hour. Each hour she picks one pile and eats up to k bananas from it. If the pile has fewer than k, she finishes it and does nothing else that hour. Return the smallest integer k that lets her finish every pile within h hours.

Example 1:
Input: piles = [1, 4, 3, 2], h = 9
Output: 2
Explanation: At k = 2 the piles take 1 + 2 + 2 + 1 = 6 hours. At k = 1 they take 10 hours, which is too many.

Example 2:
Input: piles = [25, 10, 23, 4], h = 4
Output: 25
Explanation: With one hour per pile, k must be at least the largest pile.

Example 3:
Input: piles = [3, 6, 7, 11], h = 8
Output: 4
Explanation: At k = 4 the piles take 1 + 2 + 2 + 3 = 8 hours.

Constraints:
- 1 <= len(piles) <= h <= 1,000,000
- 1 <= piles[i] <= 1,000,000,000
"""

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            k = (l + r) // 2
            if sum(math.ceil(p / k) for p in piles) <= h:
                r = k
            else:
                l = k + 1
        return l


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
