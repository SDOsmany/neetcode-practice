"""
Coin Change II (Medium)

coins lists distinct coin values, and you have unlimited coins of each. Return how many different combinations add up to amount. The order of the coins doesn't matter.

Example 1:
Input: amount = 4, coins = [1, 2, 3]
Output: 4
Explanation: 1+1+1+1, 1+1+2, 2+2 and 1+3.

Example 2:
Input: amount = 3, coins = [2]
Output: 0

Example 3:
Input: amount = 0, coins = [5]
Output: 1
Explanation: Using no coins is one way.

Constraints:
- 0 <= amount <= 5,000
- 1 <= len(coins) <= 100
"""

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
