"""
Coin Change (Medium)

coins lists coin values, and you have unlimited coins of each. Return the fewest coins that add up to amount, or -1 if it can't be done.

Example 1:
Input: coins = [1, 5, 10], amount = 12
Output: 3
Explanation: 10 + 1 + 1.

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
- 1 <= len(coins) <= 12
- 0 <= amount <= 10,000
"""

class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        best = [0] + [float("inf")] * amount
        for x in range(1, amount + 1):
            for c in coins:
                if c <= x:
                    best[x] = min(best[x], best[x - c] + 1)
        return best[amount] if best[amount] != float("inf") else -1


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
